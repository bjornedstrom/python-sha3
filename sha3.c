/* SHA3 module -- This module provides an interface to SHA-3, also
   known as Keccak.

   This code is based on sha256module.c in the standard Python 2
   distribution, which has the following header:

   ---
   Additional work performed by:

   Andrew Kuchling (amk@amk.ca)
   Greg Stein (gstein@lyra.org)
   Trevor Perrin (trevp@trevp.net)

   Copyright (C) 2005   Gregory P. Smith (greg@krypto.org)
   Licensed to PSF under a Contributor Agreement.
   ---

   This file, adapter for SHA-3, is written by Björn Edström <be@bjrn.se> 2012.

   It is placed under the same license as the original module:
   Licensed to PSF under a Contributor Agreement.
 */

#include "Python.h"
#include "structmember.h"
#include "KeccakReferenceAndOptimized/Sources/KeccakNISTInterface.h"


#define MAX_DIGEST_SIZE 64


typedef struct {
    PyObject_HEAD
    int hashbitlen;
    hashState state;
} SHAobject;


static void SHAcopy(SHAobject *src, SHAobject *dest)
{
    dest->hashbitlen = src->hashbitlen;
    memcpy(&dest->state, &src->state, sizeof(src->state));
}


static PyTypeObject SHA3type;


static SHAobject *
newSHA3object(void)
{
    return (SHAobject *)PyObject_New(SHAobject, &SHA3type);
}


static void
SHA_dealloc(PyObject *ptr)
{
    PyObject_Del(ptr);
}


PyDoc_STRVAR(SHA3_copy__doc__, "Return a copy of the hash object.");

static PyObject *
SHA3_copy(SHAobject *self, PyObject *unused)
{
    SHAobject *newobj = NULL;
    if ((newobj = newSHA3object()) == NULL) {
        return NULL;
    }
    SHAcopy(self, newobj);
    return (PyObject *)newobj;
}


PyDoc_STRVAR(SHA3_digest__doc__,
"Return the digest value as a string of binary data.");

static PyObject *
SHA3_digest(SHAobject *self, PyObject *unused)
{
    unsigned char digest[MAX_DIGEST_SIZE];
    SHAobject temp;

    SHAcopy(self, &temp);

    Final(&temp.state, digest);

    return PyString_FromStringAndSize((const char *)digest, self->hashbitlen / 8);
}


PyDoc_STRVAR(SHA3_update__doc__,
"Update this hash object's state with the provided string.");

static PyObject *
SHA3_update(SHAobject *self, PyObject *args)
{
    unsigned char *cp;
    int len;

    if (!PyArg_ParseTuple(args, "s#:update", &cp, &len))
        return NULL;

    Update(&self->state, cp, len * 8);

    Py_INCREF(Py_None);
    return Py_None;
}


PyDoc_STRVAR(SHA3_init__doc__,
"Init this hash object's state.");

static PyObject *
SHA3_init(SHAobject *self, PyObject *args)
{
    int hashbitlen;

    if (!PyArg_ParseTuple(args, "i", &hashbitlen))
        return NULL;

    self->hashbitlen = hashbitlen;
    Init(&self->state, hashbitlen);

    Py_INCREF(Py_None);
    return Py_None;
}


static PyMethodDef SHA_methods[] = {
    {"copy",      (PyCFunction)SHA3_copy,      METH_NOARGS,  SHA3_copy__doc__},
    {"digest",    (PyCFunction)SHA3_digest,    METH_NOARGS,  SHA3_digest__doc__},
    {"update",    (PyCFunction)SHA3_update,    METH_VARARGS, SHA3_update__doc__},
    {"init"  ,    (PyCFunction)SHA3_init,      METH_VARARGS, SHA3_init__doc__},
    {NULL,        NULL}         /* sentinel */
};


static PyGetSetDef SHA_getseters[] = {
    {NULL}  /* Sentinel */
};


static PyMemberDef SHA_members[] = {
    {NULL}  /* Sentinel */
};


static PyTypeObject SHA3type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "_sha3.sha3",   /*tp_name*/
    sizeof(SHAobject),  /*tp_size*/
    0,                  /*tp_itemsize*/
    /* methods */
    SHA_dealloc,        /*tp_dealloc*/
    0,                  /*tp_print*/
    0,                  /*tp_getattr*/
    0,                  /*tp_setattr*/
    0,                  /*tp_compare*/
    0,                  /*tp_repr*/
    0,                  /*tp_as_number*/
    0,                  /*tp_as_sequence*/
    0,                  /*tp_as_mapping*/
    0,                  /*tp_hash*/
    0,                  /*tp_call*/
    0,                  /*tp_str*/
    0,                  /*tp_getattro*/
    0,                  /*tp_setattro*/
    0,                  /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT, /*tp_flags*/
    0,                  /*tp_doc*/
    0,                  /*tp_traverse*/
    0,                  /*tp_clear*/
    0,                  /*tp_richcompare*/
    0,                  /*tp_weaklistoffset*/
    0,                  /*tp_iter*/
    0,                  /*tp_iternext*/
    SHA_methods,        /* tp_methods */
    SHA_members,        /* tp_members */
    SHA_getseters,      /* tp_getset */
};


PyDoc_STRVAR(SHA3_new__doc__,
"Return a new SHA-3 hash object.");

static PyObject *
SHA3_new(PyObject *self, PyObject *args, PyObject *kwdict)
{
    SHAobject *new;

    if ((new = newSHA3object()) == NULL)
        return NULL;

    if (PyErr_Occurred()) {
        Py_DECREF(new);
        return NULL;
    }

    return (PyObject *)new;
}


static struct PyMethodDef SHA_functions[] = {
    {"sha3", (PyCFunction)SHA3_new, METH_VARARGS|METH_KEYWORDS, SHA3_new__doc__},
    {NULL,      NULL}            /* Sentinel */
};


PyMODINIT_FUNC
init_sha3(void)
{
    PyObject *m;

    Py_TYPE(&SHA3type) = &PyType_Type;
    if (PyType_Ready(&SHA3type) < 0) {
        return;
    }
    m = Py_InitModule("_sha3", SHA_functions);
    if (m == NULL) {
        return;
    }
}
