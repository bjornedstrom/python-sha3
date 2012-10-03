import _sha3

class _SHA3Base(object):
    block_size = None

    def __init__(self, s=None):
        self._s = _sha3.sha3()
        self._s.init(self.digest_size * 8)
        if s is not None:
            self._s.update(s)

    def update(self, s):
        return self._s.update(s)

    def digest(self):
        return self._s.digest()

    def hexdigest(self):
        return self.digest().encode('hex')

    @property
    def digestsize(self):
        return self.digest_size


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
