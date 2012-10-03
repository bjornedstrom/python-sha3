# python-sha3 (0.1 beta)
October 3, 2012

This module implements SHA-3 (also known as Keccak) with a
`hashlib`-like interface.

The module is written as a Python C extension on top of the reference
implementation. This yields better performance than the pure Python
implementation that is available on the Keccak website.

Sample usage:

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
                       # also exposed as the function sha3.sha3_512(...)
    s.update('foo')
    print s.hexdigest()

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
    Ran 1088 tests in 0.155s
    OK

## Caveats

While reference Keccak is tweakable and can hash bit strings, this
module has the same API as the python `hashlib` module and work on
bytes only.

The current implementation most likely has a bug or two, though the
unit test coverage is fairly extensive.

## More Information

Please refer to the Keccak website for more information:

http://keccak.noekeon.org/
