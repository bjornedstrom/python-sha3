# python-sha3 (0.1 beta)
October 3, 2012

This module implements SHA-3 (also known as Keccak) with a
`hashlib`-like interface.

The module is written as a Python C extension on top of the reference
implementation. This yiels better performance than the reference
implementation in pure Python that is available on the Keccak website.

Sample usage:

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
    s.update('foo')
    print s.hexdigest()

## Building

    python setup.py build

This will require a C compilar, as usual, and also the Python
development headers.

Optionally, if you want to build a debian package:

    debuild -d -us -uc

## Caveats

While reference Keccak is tweakable and can hash bit strings, this
module has the same API as the python `hashlib` module and work on
bytes only.

The current implementation most likely has a bug or two. There could
be endian-ness issues as well.

## More Information

Please refer to the Keccak website for more information:

http://keccak.noekeon.org/
