# python-sha3 (0.2 beta)
[![Build Status](https://travis-ci.org/bjornedstrom/python-sha3.svg?branch=master)](https://travis-ci.org/bjornedstrom/python-sha3)
October 18, 2015

This module implements the SHA-3 standard as defined in FIPS202: "SHA-3 Standard:  Permutation-Based Hash and Extendable-Output Functions". More specifically, it implements the constructs:

- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512
- SHAKE128
- SHAKE256

The module is written as a Python C extension on top of optimized implementation available on the Keccak website. This yields better performance than the pure Python implementation that is available. The code is tested on various versions of Python 2 and 3.

Sample usage:

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
                       # also exposed as the function sha3.sha3_512(...)
    s.update('foo')
    print s.hexdigest()
    sk = sha3.SHAKE128(512) # also SHAKE256
    sk.update('')
    print sk.hexdigest()

Importing the `sha3` module will also add the new modules to `hashlib`.

    >>> import hashlib
    >>> import sha3
    >>> hashlib.sha3_512('foo')
    <sha3.SHA3512 object at 0x7fcd0fcb7590>

## Building

    python setup.py build

This will require a C compiler, as usual, and also the Python
development headers.

Optionally, if you want to build a debian package:

    debuild -d -us -uc

## Testing

The `test/` directory contains a bunch of unit tests. By convention
the runnable unit tests have a name that begins with `test_`, such as
the `test/test_usage.py` suite. You can run all the tests with
nosetests:

    $ nosetests test/
    ...
    Ran 1530 tests in 0.155s
    OK

## Caveats

This module limits itself to FIPS202 behavior, so none if the advanced Keccak behavior are available at the moment.

The current implementation most likely has a bug or two, though the
unit test coverage is fairly extensive.

## More Information

Please refer to the Keccak website for more information:

http://keccak.noekeon.org/

## Author

This Python module is copyright Björn Edström 2012, 2015 <be@bjrn.se>

The code is heavily based on the Keccak reference, available here:

https://github.com/gvanas/KeccakCodePackage
