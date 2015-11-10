# -*- coding: utf-8 -*-
# Copyright (c) Björn Edström <be@bjrn.se> 2012, 2015. See LICENSE for more details.

r"""hashlib-style implementation of SHA-3 winner Keccak.

This module implements SHA-3 with a haslib interface. Four classes are exposed:
SHA3224, SHA3256, SHA3384 and SHA3512. Usage should be familiar:

>>> s = SHA3512()
>>> s.update('abc')
>>> print s.hexdigest()
"""

__all__ = ['SHA3224', 'SHA3256', 'SHA3384', 'SHA3512', 'SHAKE128', 'SHAKE256',
           'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake128', 'shake256']
__version__ = '0.2beta'
__author__ = 'Bjorn Edstrom <be@bjrn.se>'

import _sha3
import binascii
import copy

class _SHA3Base(object):
    """Base class for SHA-3 implementations with different digest sizes.
    """

    _block_size = None

    def __init__(self, s=None):
        self._s = _sha3.sha3()
        self._s.init(self.digest_size * 8, self.digest_size * 8)
        if s is not None:
            self._s.update(s)

    def copy(self):
        """Return a copy of the hash object."""
        c = copy.copy(self)
        c._s = self._s.copy()
        return c

    def update(self, s):
        """Update this hash object's state with the provided string."""
        return self._s.update(s)

    def digest(self):
        """Return the digest value as a string of binary data."""
        return self._s.digest()

    def hexdigest(self):
        """Return the digest value as a string of hexadecimal digits."""
        return binascii.hexlify(self.digest())

    @property
    def digestsize(self):
        return self.digest_size

    @property
    def block_size(self):
        if self._block_size:
            return self._block_size

        # TODO (bjorn): Return something reasonable.
        raise NotImplementedError('block size not exposed')


class SHA3224(_SHA3Base):
    digest_size = 28
    _block_size = 144 / 8
    name = 'sha3-224'


class SHA3256(_SHA3Base):
    digest_size = 32
    _block_size = 136 / 8
    name = 'sha3-256'


class SHA3384(_SHA3Base):
    digest_size = 48
    _block_size = 104 / 8
    name = 'sha3-384'


class SHA3512(_SHA3Base):
    digest_size = 64
    _block_size = 72 / 8
    name = 'sha3-512'


def sha3_224(s=None):
    """Returns a sha3-224 hash object; optionally initialized with a string"""
    return SHA3224(s)


def sha3_256(s=None):
    """Returns a sha3-256 hash object; optionally initialized with a string"""
    return SHA3256(s)


def sha3_384(s=None):
    """Returns a sha3-384 hash object; optionally initialized with a string"""
    return SHA3384(s)


def sha3_512(s=None):
    """Returns a sha3-512 hash object; optionally initialized with a string"""
    return SHA3512(s)


class _SHAKEBase(_SHA3Base):
    def __init__(self, output_length=0):
        if output_length % 8:
            raise NotImplementedError('output bit lengths that are not a multiple of 8 bits: not tested yet')
        self._s = _sha3.sha3()
        self._s.init(self._internal_id, output_length)

    def squeeze(self, output_length):
        return self._s.squeeze(output_length)


class SHAKE128(_SHAKEBase):
    _internal_id = 10128


class SHAKE256(_SHAKEBase):
    _internal_id = 10256


def shake128(output_length, s=None):
    obj = SHAKE128(output_length)
    if s:
        obj.update(s)
    return obj


def shake256(output_length, s=None):
    obj = SHAKE256(output_length)
    if s:
        obj.update(s)
    return obj


try:
    import hashlib
    setattr(hashlib, 'sha3_224', sha3_224)
    setattr(hashlib, 'sha3_256', sha3_256)
    setattr(hashlib, 'sha3_384', sha3_384)
    setattr(hashlib, 'sha3_512', sha3_512)

    setattr(hashlib, 'shake128', shake128)
    setattr(hashlib, 'shake256', shake256)
except:
    pass
