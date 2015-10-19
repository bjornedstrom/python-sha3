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

## Please Note

The FIPS202 specification is slightly different from the Keccak version that won the SHA-3 competition a few years ago. Many of the "sha3" or "keccak" libraries out there (including many for Python) are not FIPS202 compatible, so they compute different results.

This module aims to be FIPS202 compatible.

## Usage

### SHA-3

The `SHA3*` functions are written to be as similar as possible to `hashlib`:

Sample usage:

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
                       # also exposed as the function sha3.sha3_512(...)
    s.update('foo')
    print(s.hexdigest())

Importing the `sha3` module will also add the new modules to `hashlib`.

    >>> import hashlib
    >>> import sha3
    >>> hashlib.sha3_512('foo')
    <sha3.SHA3512 object at 0x7fcd0fcb7590>

### SHAKE

The SHAKE functions are Extendable-Output Functions (XOF:s) which are different from hash functions. The interface is similar to `hashlib`. You can either give the output length (in bits) at initialization time or digest computation time:

Alternative 1:

    sk = sha3.SHAKE128(512) # also SHAKE256
    sk.update('')
    print([sk.digest()])

Alternative 2:

    sk = sha3.SHAKE128() # also SHAKE256
    sk.update('')
    print([sk.squeeze(512)])

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

- This module limits itself to FIPS202 behavior, so none if the advanced Keccak behavior are available at the moment.
- At the moment, this code work on byte strings only (i.e. input and output strings must be a multiple if 8 bits).
- Calling the C module directly is a little bit flaky, so it's recommended you only use the functions and classes available from `import sha3`.
- The current implementation most likely has a bug or two, though the unit test coverage is fairly extensive.

## More Information

Please refer to the Keccak website for more information:

http://keccak.noekeon.org/

## Author

This Python module is copyright Björn Edström 2012, 2015 <be@bjrn.se>

The code is heavily based on the Keccak reference which is available here:

https://github.com/gvanas/KeccakCodePackage
