# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

_sha3 = Extension('_sha3',
                  include_dirs = [
                      'src/',
                      'src/64'],
                  sources = ['sha3.c',
                             'src/KeccakHash.c',
                             'src/KeccakSponge.c',
                             'src/64/KeccakF-1600-opt64.c'])

setup(name='sha3',
      version='0.2.1',
      description='SHA-3 implementation for Python',
      author=u'Björn Edström',
      author_email='be@bjrn.se',
      url='https://github.com/bjornedstrom/python-sha3',
      ext_modules=[_sha3],
      packages=['sha3'])
