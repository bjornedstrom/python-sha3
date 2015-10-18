import sha3
import unittest

class SHA3UsageTests(unittest.TestCase):

    def test_copy(self):
        a = sha3.SHA3224()
        a.update(b'foo')
        b = a.copy()
        assert a.digest() == b.digest()
        b.update(b'bar')
        assert a.digest() != b.digest()

    def test_digest_size(self):
        a = sha3.SHA3224()
        assert len(a.digest()) == a.digest_size

    def test_name(self):
        a = sha3.SHA3224()
        assert a.name == 'sha3-224'

    def test_constructor(self):
        a = sha3.SHA3224('')
        self.assertEquals(a.hexdigest(), b'6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7')

    def test_update(self):
        a = sha3.SHA3224()
        a.update('')
        assert a.hexdigest() == b'6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7'

    def test_updates(self):
        a = sha3.SHA3512()
        a.update(b'\xee\xd7')
        a.update(b'\x42\x22\x27\x61\x3B\x6F\x53\xC9')
        assert a.hexdigest() == b'5A566FB181BE53A4109275537D80E5FD0F314D68884529CA66B8B0E9F240A673B64B28FFFE4C1EC4A5CEF0F430229C5757EBD172B4B0B68A81D8C58A9E96E164'.lower()

    def test_empty_sha3224(self):
        a = sha3.SHA3224()
        assert a.hexdigest() == b'6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7'

    def test_empty_sha3256(self):
        a = sha3.SHA3256()
        assert a.hexdigest() == b'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'

    def test_empty_sha3384(self):
        a = sha3.SHA3384()
        assert a.hexdigest() == b'0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004'

    def test_empty_sha3512(self):
        a = sha3.SHA3512()
        assert a.hexdigest() == b'a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26'


if __name__ == '__main__':
    unittest.main()
