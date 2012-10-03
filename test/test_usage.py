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


if __name__ == '__main__':
    unittest.main()
