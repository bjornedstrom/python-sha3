import sha3
import unittest

class SHA3UsageTests(unittest.TestCase):

    def test_copy(self):
        a = sha3.SHA3224()
        a.update('foo')
        b = a.copy()
        assert a.digest() == b.digest()
        b.update('bar')
        assert a.digest() != b.digest()

    def test_digest_size(self):
        a = sha3.SHA3224()
        assert len(a.digest()) == a.digest_size

    def test_name(self):
        a = sha3.SHA3224()
        assert a.name == 'sha3-224'

    def test_constructor(self):
        a = sha3.SHA3224('\xcc')
        assert a.hexdigest() == 'a9cab59eb40a10b246290f2d6086e32e3689faf1d26b470c899f2802'

    def test_update(self):
        a = sha3.SHA3224()
        a.update('\xcc')
        assert a.hexdigest() == 'a9cab59eb40a10b246290f2d6086e32e3689faf1d26b470c899f2802'

    def test_updates(self):
        a = sha3.SHA3224()
        a.update('\x21')
        a.update('\xf1\x34')
        a.update('\xac\x57')
        assert a.hexdigest() == '5573da2b02216a860389a581f6e9fb8d805e9e02f6fa911701eee298'

    def test_empty_sha3224(self):
        a = sha3.SHA3224()
        assert a.hexdigest() == 'f71837502ba8e10837bdd8d365adb85591895602fc552b48b7390abd'

    def test_empty_sha3256(self):
        a = sha3.SHA3256()
        assert a.hexdigest() == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'

    def test_empty_sha3384(self):
        a = sha3.SHA3384()
        assert a.hexdigest() == '2c23146a63a29acf99e73b88f8c24eaa7dc60aa771780ccc006afbfa8fe2479b2dd2b21362337441ac12b515911957ff'

    def test_empty_sha3512(self):
        a = sha3.SHA3512()
        assert a.hexdigest() == '0eab42de4c3ceb9235fc91acffe746b29c29a8c366b7c60e4e67c466f36a4304c00fa9caf9d87976ba469bcbe06713b435f091ef2769fb160cdab33d3670680e'


if __name__ == '__main__':
    unittest.main()
