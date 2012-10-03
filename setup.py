# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

_sha3 = Extension('_sha3',
                 sources = ['sha3.c',
                            'KeccakReferenceAndOptimized/Sources/KeccakNISTInterface.c',
                            'KeccakReferenceAndOptimized/Sources/KeccakSponge.c',
                            'KeccakReferenceAndOptimized/Sources/KeccakF-1600-reference.c',
                            'KeccakReferenceAndOptimized/Sources/displayIntermediateValues.c'])

setup(name='_sha3',
      version='0.1',
      description='SHA-3 implementation for Python',
      author=u'Björn Edström',
      author_email='be@bjrn.se',
      url='https://github.com/bjornedstrom/python-sha3',
      ext_modules=[_sha3],
      packages=['sha3'])
