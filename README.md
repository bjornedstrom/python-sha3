# python-sha3

A fast `hashlib` style Python implementation of SHA-3 (Keccak)
implemented in C, on top of the Keccak reference implementation.

Sample usage:

    import sha3
    s = sha3.SHA3512() # also 224, 256, 384, 512
    s.update('foo')
    print s.hexdigest()

## Building

    python setup.py build

## Caveats

While Keccak is tweakable, can hash on a bit level etc, this module is
not. It works on byte arrays only. It also works with the select block
sizes only.

There are probably bugs. Possibly endianness-issues.
