# -*- coding: utf-8 -*-
import os, shutil

version = '3.2.5'

class KeccakInstance:
    def __init__(self, r, c, n=0):
        self.r = r
        self.c = c
        self.n = n
        self.name = 'keccak'
        if (r+c != 1600):
            self.name = self.name + 'r{0}'.format(r) + 'c{0}'.format(c)
        elif (c != 576):
            self.name = self.name + 'c{0}'.format(c)
    def outputSize(self):
        if (self.n != 0):
            return self.n
        else:
            return self.r
    def outputSizeIsRate(self):
        if (self.n != 0):
            return False
        else:
            return True

def makeDir(instance, implementation):
    pathName = instance.name + '/' + implementation
    try:
        os.makedirs(pathName)
    except OSError:
        pass

def copySourceFiles(instance, implementation, sourceFiles, sourceLocation='Sources/'):
    for fileName in sourceFiles:
        shutil.copyfile('../'+sourceLocation+fileName, instance.name+'/'+implementation+'/'+fileName)

def writeAPIdotH(instance, implementation):
    with open(instance.name+'/'+implementation+'/api.h', 'w') as f:
        f.write('#define CRYPTO_BYTES {0}\n'.format(instance.outputSize()//8))
        f.write('#define CRYPTO_VERSION "{0}"\n'.format(version))

def copyWrapperFiles(instance, implementation):
    shutil.copyfile('hash-'+instance.name+'.c', instance.name+'/'+implementation+'/hash.c')
    shutil.copyfile('int-set-'+instance.name+'.h', instance.name+'/'+implementation+'/KeccakF-1600-int-set.h')

def writeImplementors(instance, implementation, implementors):
    with open(instance.name+'/'+implementation+'/implementors', 'w') as f:
        for person in implementors:
            f.write(person+'\n')

Ronny = ['Ronny Van Keer']
Designers = ['Guido Bertoni', 'Joan Daemen', 'Michaël Peeters', 'Gilles Van Assche']

def makeOpt64(instance, laneComplementing, unrolling, useSHLD=False):
    implementation = 'opt64'
    if (laneComplementing):
        implementation = implementation + 'lc'
    implementation = implementation + 'u{0}'.format(unrolling)
    if (useSHLD):
        implementation = implementation + 'shld'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    with open(instance.name+'/'+implementation+'/KeccakF-1600-opt64-settings.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        if (laneComplementing):
            f.write('#define UseBebigokimisa\n')
        if (useSHLD):
            f.write('#define UseSHLD\n')
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-unrolling.macros',
                      'KeccakF-1600-64.macros',
                      'KeccakF-1600-opt64.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    writeImplementors(instance, implementation, Designers)

def makeOpt_x86_64_asm(instance):
    implementation = 'x86_64_asm'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-x86-64-gas.s',
                      'KeccakF-1600-x86-64-asm.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
    writeImplementors(instance, implementation, Ronny)

def makeOpt_x86_64_shld(instance):
    implementation = 'x86_64_shld'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-x86-64-shld-gas.s',
                      'KeccakF-1600-x86-64-asm.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
    writeImplementors(instance, implementation, Ronny)

def makeSSE(instance, unrolling):
    implementation = 'sse'
    implementation = implementation + 'u{0}'.format(unrolling)
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    with open(instance.name+'/'+implementation+'/KeccakF-1600-opt64-settings.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        f.write('#define UseSSE\n')
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-unrolling.macros',
                      'KeccakF-1600-simd128.macros',
                      'KeccakF-1600-opt64.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
        f.write('x86\n')
    writeImplementors(instance, implementation, Designers)

def makeXOP(instance, unrolling):
    implementation = 'xop'
    implementation = implementation + 'u{0}'.format(unrolling)
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    with open(instance.name+'/'+implementation+'/KeccakF-1600-opt64-settings.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        f.write('#define UseXOP\n')
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-unrolling.macros',
                      'KeccakF-1600-xop.macros',
                      'KeccakF-1600-opt64.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
        f.write('x86\n')
    writeImplementors(instance, implementation, Designers)

def makeMMX(instance, unrolling):
    implementation = 'mmx'
    implementation = implementation + 'u{0}'.format(unrolling)
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    with open(instance.name+'/'+implementation+'/KeccakF-1600-opt64-settings.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        f.write('#define UseMMX\n')
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-unrolling.macros',
                      'KeccakF-1600-simd64.macros',
                      'KeccakF-1600-opt64.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
        f.write('x86\n')
    writeImplementors(instance, implementation, Designers)

def makeOpt32(instance, bitInterleavingTable, laneComplementing, schedule, unrolling):
    implementation = 'opt32bi'
    if (bitInterleavingTable):
        implementation = implementation + 'T'
    if (schedule == 3):
        implementation = implementation + '-rvk'
    else:
        implementation = implementation + '-s{0}'.format(schedule)
    if (laneComplementing):
        implementation = implementation + 'lc'
    implementation = implementation + 'u{0}'.format(unrolling)
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    with open(instance.name+'/'+implementation+'/KeccakF-1600-opt32-settings.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        if (bitInterleavingTable):
            f.write('#define UseInterleaveTables\n')
        if (laneComplementing):
            f.write('#define UseBebigokimisa\n')
        f.write('#define UseSchedule {0}\n'.format(schedule))
    copySourceFiles(instance, implementation,
                    [ 'brg_endian.h',
                      'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-unrolling.macros',
                      'KeccakF-1600-32.macros',
                      'KeccakF-1600-opt32.c' ])
    if (schedule == 3):
        copySourceFiles(instance, implementation, ['KeccakF-1600-32-rvk.macros'])
    else:
        copySourceFiles(instance, implementation, ['KeccakF-1600-32-s{0}.macros'.format(schedule)])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    if (schedule == 3):
        writeImplementors(instance, implementation, Designers + Ronny)
    else:
        writeImplementors(instance, implementation, Designers)

def architectureARM(instance, implementation):
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('arm\n')
        f.write('armeabi\n')

def makeARMasm(instance):
    implementation = 'armasm'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'KeccakSponge.c',
                      'KeccakSponge.h',
                      'KeccakF-1600-interface.h',
                      'KeccakF-1600-armgcc.s',
                      'KeccakF-1600-arm.c' ])
    writeAPIdotH(instance, implementation)
    copyWrapperFiles(instance, implementation)
    architectureARM(instance, implementation)
    writeImplementors(instance, implementation, Ronny)

def makeSimple(instance):
    implementation = 'simple'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-simple.c' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-simple-settings.h')
    writeImplementors(instance, implementation, Ronny)

def makeSimple32BI(instance):
    implementation = 'simple32bi'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-simple32BI.c' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-simple-settings.h')
    writeImplementors(instance, implementation, Designers + Ronny)

def makeInplace(instance):
    implementation = 'inplace'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-inplace.c' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-inplace-settings.h')
    writeImplementors(instance, implementation, Designers + Ronny)

def makeInplace32BI(instance):
    implementation = 'inplace32bi'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-inplace32BI.c' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-inplace-settings.h')
    writeImplementors(instance, implementation, Designers + Ronny)

def processAssemblyCode(instance, implementation, source, destination):
    with open(source, 'r') as f:
        d = open(destination, 'w')
        for line in f:
            if (line.find('// populate.py, please set cKeccakR_SizeInBytes') >= 0):
                d.write('.equ cKeccakR_SizeInBytes , {0}/8\n'.format(instance.r))
            elif (line.find('// populate.py, please set crypto_hash_BYTES') >= 0):
                if (instance.outputSizeIsRate()):
                    d.write('.equ crypto_hash_BYTES , cKeccakR_SizeInBytes\n')
                else:
                    d.write('.equ crypto_hash_BYTES , {0}/8\n'.format(instance.outputSize()))
            elif (line.find('// populate.py, please update crypto_hash') >= 0):
                line = line[0:line.find('// populate.py, please update crypto_hash')]
                crypto_hash = 'crypto_hash_'+instance.name+'_'+implementation.replace('-', '_')
                line = line.replace('crypto_hash', crypto_hash)
                d.write(line+'\n')
            else:
                d.write(line)

def makeInplace32BI_ARMv6M(instance):
    implementation = 'inplace32bi-armv6m'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    processAssemblyCode(instance, implementation, '../Sources/Keccak-inplace32BI-armgcc-ARMv6M.s', instance.name+'/'+implementation+'/Keccak-inplace32BI-armgcc-ARMv6M.s')
    writeAPIdotH(instance, implementation)
    architectureARM(instance, implementation)
    writeImplementors(instance, implementation, Ronny)

def makeInplace32BI_ARMv7M(instance):
    implementation = 'inplace32bi-armv7m'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    processAssemblyCode(instance, implementation, '../Sources/Keccak-inplace32BI-armgcc-ARMv7M.s', instance.name+'/'+implementation+'/Keccak-inplace32BI-armgcc-ARMv7M.s')
    writeAPIdotH(instance, implementation)
    architectureARM(instance, implementation)
    writeImplementors(instance, implementation, Ronny)

def makeInplace32BI_ARMv7A(instance):
    implementation = 'inplace32bi-armv7a'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    processAssemblyCode(instance, implementation, '../Sources/Keccak-inplace32BI-armgcc-ARMv7A.s', instance.name+'/'+implementation+'/Keccak-inplace32BI-armgcc-ARMv7A.s')
    writeAPIdotH(instance, implementation)
    architectureARM(instance, implementation)
    writeImplementors(instance, implementation, Ronny)

def makeInplace_ARMv7A_NEON(instance):
    implementation = 'inplace-armv7a-neon'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    writeAPIdotH(instance, implementation)
    fileName = instance.name.replace('keccak', 'Keccak')+'-crypto_hash-inplace-armgcc-ARMv7A-NEON.s'
    processAssemblyCode(instance, implementation, '../Sources/'+fileName, instance.name+'/'+implementation+'/Keccak.s')
    shutil.copyfile('../Sources/KeccakF-1600-inplace-armgcc-ARMv7A-NEON.s', instance.name+'/'+implementation+'/Keccak2.s')
    writeImplementors(instance, implementation, Ronny)

def makeCompact(instance):
    implementation = 'compact'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-compact.c',
                      'Keccak-compact.h' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-compact-settings.h')
    writeImplementors(instance, implementation, Ronny)

def makeCompact8(instance):
    implementation = 'compact8'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-compact8.c',
                      'Keccak-compact8.h' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-compact8-settings.h')
    writeImplementors(instance, implementation, Designers + Ronny)

def makeAVR8(instance):
    implementation = 'avr8'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'AVR8-rotate64.h',
                      'AVR8-rotate64.s',
                      'Keccak-avr8.c',
                      'Keccak-avr8.h',
                      'Keccak-avr8-util.h',
                      'Keccak-avr8-util.s',
                      'KeccakF-1600-avr8.c' ])
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-avr8-settings.h')
    writeImplementors(instance, implementation, Ronny)

def makeAVR8asmCompact(instance):
    implementation = 'avr8asmc'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-avr8.h' ])
    processAssemblyCode(instance, implementation, '../Sources/KeccakF-1600-avr8asm-compact.s', instance.name+'/'+implementation+'/KeccakF-1600-avr8asm-compact.s')
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-avr8-settings.h')
    writeImplementors(instance, implementation, Ronny)

def makeAVR8asmFast(instance):
    implementation = 'avr8asmf'
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    copySourceFiles(instance, implementation,
                    [ 'Keccak-avr8.h' ])
    processAssemblyCode(instance, implementation, '../Sources/KeccakF-1600-avr8asm-fast.s', instance.name+'/'+implementation+'/KeccakF-1600-avr8asm-fast.s')
    writeAPIdotH(instance, implementation)
    shutil.copyfile('simple-'+instance.name+'.h', instance.name+'/'+implementation+'/Keccak-avr8-settings.h')
    writeImplementors(instance, implementation, Ronny)

def eBASH_Keccak(r, c, n=0):
    instance = KeccakInstance(r, c, n)
    print('Instance', instance.name)
    makeOpt_x86_64_asm(instance)
    makeOpt_x86_64_shld(instance)
    makeOpt64(instance, True, 24, True)
    makeOpt64(instance, True, 24)
    makeOpt64(instance, True, 6)
    makeOpt64(instance, False, 6)
    makeOpt32(instance, False, True, 2, 4)
    makeOpt32(instance, True, True, 2, 4)
    #makeOpt32(instance, False, False, 2, 4)
    makeOpt32(instance, False, False, 3, 2)
    #makeOpt32(instance, False, True, 1, 4)
    makeSSE(instance, 2)
    makeXOP(instance, 24)
    makeMMX(instance, 1)
    #makeARMasm(instance)
    makeSimple(instance)
    makeSimple32BI(instance)
    makeInplace(instance)
    if ((r+c == 1600) and (c in [512, 576, 1024])):
        makeInplace_ARMv7A_NEON(instance)
    makeInplace32BI(instance)
    makeInplace32BI_ARMv6M(instance)
    makeInplace32BI_ARMv7M(instance)
    makeInplace32BI_ARMv7A(instance)
    makeCompact(instance)
    makeCompact8(instance)
    makeAVR8(instance)
    makeAVR8asmCompact(instance)
    makeAVR8asmFast(instance)
    shutil.copyfile('checksum-'+instance.name, instance.name+'/checksum')

class ShortLeafInterleavedKeccakTreeInstance:
    def __init__(self, r, c, D, B, n=0):
        self.r = r
        self.c = c
        self.D = D
        self.B = B
        self.n = n
        self.name = 'keccak'
        if (r+c != 1600):
            self.name = self.name + 'r{0}'.format(r) + 'c{0}'.format(c)
        elif (c != 576):
            self.name = self.name + 'c{0}'.format(c)
        self.name = self.name + 'treed{0}'.format(D)
        if (B != 64):
            self.name = self.name + 'b{0}'.format(B)
    def outputSize(self):
        if (self.n != 0):
            return self.n
        else:
            return self.r
    def outputSizeIsRate(self):
        if (self.n != 0):
            return False
        else:
            return True
    
def makeTree(instance, unrolling, implBaseName, useWhat):
    implementation = implBaseName
    implementation = implementation + 'u{0}'.format(unrolling)
    print('  Implementation', implementation)
    makeDir(instance, implementation)
    if (instance.D != 2):
        raise "D must be 2"
    with open(instance.name+'/'+implementation+'/DoublePermutation-config.h', 'w') as f:
        f.write('#define Unrolling {0}\n'.format(unrolling))
        f.write('#define '+useWhat+'\n')
    hashFileName = instance.name.replace('keccak', 'Keccak').replace('tree', 'Tree').replace('d', 'D')
    copySourceFiles(instance, implementation,
                    [ 'DoublePermutation.c',
                      'DoublePermutation.h',
                      hashFileName+'.c',
                      hashFileName+'.h',
                      'KeccakF-1600-unrolling.macros' ],
                    'TreeHashing/Sources/')
    writeAPIdotH(instance, implementation)
    with open(instance.name+'/'+implementation+'/architectures', 'w') as f:
        f.write('amd64\n')
        f.write('x86\n')
    writeImplementors(instance, implementation, Designers)

def makeTreeSSE(instance, unrolling):
    makeTree(instance, unrolling, 'sse', 'UseSSE')
    
def makeTreeXOP(instance, unrolling):
    makeTree(instance, unrolling, 'xop', 'UseXOP')
    
def eBASH_KeccakTree(r, c, D, B, n=0):
    instance = ShortLeafInterleavedKeccakTreeInstance(r, c, D, B, n)
    print('Instance', instance.name)
    makeTreeSSE(instance, 4)
    makeTreeSSE(instance, 24)
    makeTreeXOP(instance, 24)
    shutil.copyfile('checksum-'+instance.name, instance.name+'/checksum')

    
eBASH_Keccak(r=576, c=1024, n=512)
eBASH_Keccak(r=832, c=768, n=384)
eBASH_Keccak(r=1024, c=576)
eBASH_Keccak(r=1088, c=512, n=256)
eBASH_Keccak(r=1152, c=448, n=224)
eBASH_Keccak(r=1344, c=256)
eBASH_KeccakTree(r=1088, c=512, D=2, B=64)
eBASH_KeccakTree(r=1344, c=256, D=2, B=64)
