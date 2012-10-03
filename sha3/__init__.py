# -*- coding: utf-8 -*-
# Copyright (c) Björn Edström <be@bjrn.se> 2012. See LICENSE for more details.

r"""hashlib-style implementation of SHA-3 winner Keccak.

This module implements SHA-3 with a haslib interface. Four classes are exposed:
SHA3224, SHA3256, SHA3384 and SHA3512. Usage should be familiar:

>>> s = SHA3512()
>>> s.update('abc')
>>> print s.hexdigest()
"""

__all__ = ['SHA3224', 'SHA3256', 'SHA3384', 'SHA3512',
           'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']
__version__ = '0.1beta'
__author__ = 'Bjorn Edstrom <be@bjrn.se>'

import _sha3
import copy

class _SHA3Base(object):
    """Base class for SHA-3 implementations with different digest sizes.
    """

    def __init__(self, s=None):
        self._s = _sha3.sha3()
        self._s.init(self.digest_size * 8)
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
        return self.digest().encode('hex')

    @property
    def digestsize(self):
        return self.digest_size

    @property
    def block_size(self):
        # TODO (bjorn): Return something reasonable.
        raise NotImplementedError('block size not exposed')


class SHA3224(_SHA3Base):
    digest_size = 28
    name = 'sha3-224'


class SHA3256(_SHA3Base):
    digest_size = 32
    name = 'sha3-256'


class SHA3384(_SHA3Base):
    digest_size = 48
    name = 'sha3-384'


class SHA3512(_SHA3Base):
    digest_size = 64
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


try:
    import hashlib
    setattr(hashlib, 'sha3_224', sha3_224)
    setattr(hashlib, 'sha3_256', sha3_256)
    setattr(hashlib, 'sha3_384', sha3_384)
    setattr(hashlib, 'sha3_512', sha3_512)
except:
    pass
