import sha3
import unittest

class SHA3Tests(unittest.TestCase):

    FILES = [
        ('test/data/ShortMsgKAT_224.txt', sha3.SHA3224),
        ('test/data/ShortMsgKAT_256.txt', sha3.SHA3256),
        ('test/data/ShortMsgKAT_384.txt', sha3.SHA3384),
        ('test/data/ShortMsgKAT_512.txt', sha3.SHA3512),
        ('test/data/LongMsgKAT_224.txt', sha3.SHA3224),
        ]

    def test_from_files(self):
        num_tests = 0
        for path, instance in self.FILES:
            print path
            contents = file(path).read().split('Len = ')
            for test in contents:
                lines = test.split('\n')
                if lines and len(lines) and not lines[0].startswith('#'):
                    length = int(lines[0])
                    if length % 8 == 0 and length != 0:
                        msg = lines[1].split(' = ')[-1]
                        md = lines[2].split(' = ')[-1]

                        h = instance()
                        h.update(msg.decode('hex'))
                        try:
                            assert h.hexdigest().upper() == md
                            num_tests += 1
                        except:
                            print path
                            print test
                            print (msg.decode('hex'), h.hexdigest().upper(), md)
                            raise
        print 'Ran %d tests.' % (num_tests,)


if __name__ == '__main__':
    unittest.main()
