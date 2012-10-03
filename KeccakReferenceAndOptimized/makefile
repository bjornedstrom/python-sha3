all: KeccakReference KeccakReference32BI KeccakOptimized32 KeccakOptimized64 KeccakSimple KeccakSimple32BI KeccakCompact

SOURCES_COMMON = \
    Sources/genKAT.c \
    Sources/KeccakDuplex.c \
    Sources/KeccakNISTInterface.c \
    Sources/KeccakSponge.c

SOURCES_REFERENCE = \
    $(SOURCES_COMMON) \
    Sources/displayIntermediateValues.c \
    Sources/KeccakF-1600-reference.c \
    Sources/mainReference.c

SOURCES_REFERENCE32BI = \
    $(SOURCES_COMMON) \
    Sources/displayIntermediateValues.c \
    Sources/KeccakF-1600-reference32BI.c \
    Sources/mainReference.c

SOURCES_OPTIMIZED = \
    $(SOURCES_COMMON) \
    Sources/mainOptimized.c \
    Sources/timing.c

SOURCES_OPTIMIZED_32 = \
    $(SOURCES_OPTIMIZED) \
    Sources/KeccakF-1600-opt32.c

SOURCES_OPTIMIZED_64 = \
    $(SOURCES_OPTIMIZED) \
    Sources/KeccakF-1600-opt64.c

SOURCES_OPTIMIZED_64_ASM = \
    $(SOURCES_OPTIMIZED) \
    Sources/KeccakF-1600-x86-64-gas.s \
    Sources/KeccakF-1600-x86-64-asm.c

SOURCES_SIMPLE = \
    Sources/Keccak-simple.c \
    Sources/Keccak-simple-test.c

SOURCES_SIMPLE32BI = \
    Sources/Keccak-simple32BI.c \
    Sources/Keccak-simple-test.c

SOURCES_INPLACE = \
    Sources/Keccak-inplace.c \
    Sources/Keccak-inplace-test.c

SOURCES_INPLACE32BI = \
    Sources/Keccak-inplace32BI.c \
    Sources/Keccak-inplace-test.c

SOURCES_COMPACT = \
    Sources/Keccak-compact.c \
    Sources/Keccak-compact-test.c

SOURCES_COMPACT8 = \
    Sources/Keccak-compact8.c \
    Sources/Keccak-compact8-test.c

HEADERS_COMMON = \
    Sources/KeccakDuplex.h \
    Sources/KeccakNISTInterface.h \
    Sources/KeccakSponge.h \
    Sources/KeccakF-1600-interface.h

HEADERS_REFERENCE = \
    $(HEADERS_COMMON) \
    Sources/displayIntermediateValues.h \
    Sources/KeccakF-1600-reference.h

HEADERS_REFERENCE32BI = $(HEADERS_REFERENCE)

HEADERS_OPTIMIZED = \
    $(HEADERS_COMMON) \
    Sources/timing.h \
    Sources/brg_endian.h \
    Sources/KeccakF-1600-unrolling.macros

HEADERS_OPTIMIZED_32 = \
    $(HEADERS_OPTIMIZED) \
    Sources/KeccakF-1600-opt32-settings.h \
    Sources/KeccakF-1600-32.macros \
    Sources/KeccakF-1600-32-s1.macros \
    Sources/KeccakF-1600-32-s2.macros \
    Sources/KeccakF-1600-32-rvk.macros

HEADERS_OPTIMIZED_64 = \
    $(HEADERS_OPTIMIZED) \
    Sources/KeccakF-1600-opt64-settings.h \
    Sources/KeccakF-1600-64.macros \
    Sources/KeccakF-1600-simd64.macros \
    Sources/KeccakF-1600-simd128.macros

HEADERS_OPTIMIZED_64_ASM = $(HEADERS_OPTIMIZED)

HEADERS_SIMPLE = \
    Sources/Keccak-simple-settings.h

HEADERS_SIMPLE32BI = $(HEADERS_SIMPLE)

HEADERS_INPLACE = \
    Sources/Keccak-inplace-settings.h

HEADERS_INPLACE32BI = $(HEADERS_INPLACE)

HEADERS_COMPACT = \
    Sources/Keccak-compact.h \
    Sources/Keccak-compact-settings.h

HEADERS_COMPACT8 = \
    Sources/Keccak-compact8.h \
    Sources/Keccak-compact8-settings.h

BINDIR_REFERENCE = bin/reference

$(BINDIR_REFERENCE):
	mkdir -p $(BINDIR_REFERENCE)

BINDIR_REFERENCE32BI = bin/reference32bi

$(BINDIR_REFERENCE32BI):
	mkdir -p $(BINDIR_REFERENCE32BI)

BINDIR_OPTIMIZED_32 = bin/optimized32

$(BINDIR_OPTIMIZED_32):
	mkdir -p $(BINDIR_OPTIMIZED_32)

BINDIR_OPTIMIZED_64 = bin/optimized64

$(BINDIR_OPTIMIZED_64):
	mkdir -p $(BINDIR_OPTIMIZED_64)

BINDIR_OPTIMIZED_64_ASM = bin/optimized64asm

$(BINDIR_OPTIMIZED_64_ASM):
	mkdir -p $(BINDIR_OPTIMIZED_64_ASM)

BINDIR_SIMPLE = bin/simple

$(BINDIR_SIMPLE):
	mkdir -p $(BINDIR_SIMPLE)

BINDIR_SIMPLE32BI = bin/simple32BI

$(BINDIR_SIMPLE32BI):
	mkdir -p $(BINDIR_SIMPLE32BI)

BINDIR_INPLACE = bin/inplace

$(BINDIR_INPLACE):
	mkdir -p $(BINDIR_INPLACE)

BINDIR_INPLACE32BI = bin/inplace32BI

$(BINDIR_INPLACE32BI):
	mkdir -p $(BINDIR_INPLACE32BI)

BINDIR_COMPACT = bin/compact

$(BINDIR_COMPACT):
	mkdir -p $(BINDIR_COMPACT)

BINDIR_COMPACT8 = bin/compact8

$(BINDIR_COMPACT8):
	mkdir -p $(BINDIR_COMPACT8)

OBJECTS_REFERENCE = $(addprefix $(BINDIR_REFERENCE)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_REFERENCE))))

OBJECTS_REFERENCE32BI = $(addprefix $(BINDIR_REFERENCE32BI)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_REFERENCE32BI))))

OBJECTS_OPTIMIZED_32 = $(addprefix $(BINDIR_OPTIMIZED_32)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_OPTIMIZED_32))))

OBJECTS_OPTIMIZED_64 = $(addprefix $(BINDIR_OPTIMIZED_64)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_OPTIMIZED_64))))

OBJECTS_OPTIMIZED_64_ASM = $(addprefix $(BINDIR_OPTIMIZED_64_ASM)/, $(notdir $(patsubst %.c,%.o,$(patsubst %.s,%.o,$(SOURCES_OPTIMIZED_64_ASM)))))

OBJECTS_SIMPLE = $(addprefix $(BINDIR_SIMPLE)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_SIMPLE))))

OBJECTS_SIMPLE32BI = $(addprefix $(BINDIR_SIMPLE32BI)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_SIMPLE32BI))))

OBJECTS_INPLACE = $(addprefix $(BINDIR_INPLACE)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_INPLACE))))

OBJECTS_INPLACE32BI = $(addprefix $(BINDIR_INPLACE32BI)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_INPLACE32BI))))

OBJECTS_COMPACT = $(addprefix $(BINDIR_COMPACT)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_COMPACT))))

OBJECTS_COMPACT8 = $(addprefix $(BINDIR_COMPACT8)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_COMPACT8))))

CC = gcc
#CC = icc

CFLAGS_REFERENCE = -DKeccakReference -O

CFLAGS_REFERENCE32BI = $(CFLAGS_REFERENCE) -DKeccakReference32BI

CFLAGS_OPTIMIZED_32 = -fomit-frame-pointer -O3 -g0 -march=nocona -m32
#CFLAGS_OPTIMIZED_32 = -m32 -O3 -static

CFLAGS_OPTIMIZED_64 = -fomit-frame-pointer -O3 -g0 -march=native -mtune=native -m64
#CFLAGS_OPTIMIZED_64 = -fomit-frame-pointer -O3 -g0 -march=barcelona -m32
#CFLAGS_OPTIMIZED_64 = -m64 -O3 -static

CFLAGS_OPTIMIZED_64_ASM = $(CFLAGS_OPTIMIZED_64)

CFLAGS_SIMPLE = -O3 -g0

CFLAGS_SIMPLE32BI = $(CFLAGS_SIMPLE)

CFLAGS_INPLACE = -O3 -g0

CFLAGS_INPLACE32BI = $(CFLAGS_INPLACE)

CFLAGS_COMPACT = -O3 -g0

CFLAGS_COMPACT8 = $(CFLAGS_COMPACT)

VPATH = Sources

INCLUDES = -ISources

$(BINDIR_REFERENCE)/%.o:%.c $(HEADERS_REFERENCE)
	$(CC) $(INCLUDES) $(CFLAGS_REFERENCE) -c $< -o $@

$(BINDIR_REFERENCE32BI)/%.o:%.c $(HEADERS_REFERENCE32BI)
	$(CC) $(INCLUDES) $(CFLAGS_REFERENCE32BI) -c $< -o $@

$(BINDIR_OPTIMIZED_32)/%.o:%.c $(HEADERS_OPTIMIZED_32)
	$(CC) $(INCLUDES) $(CFLAGS_OPTIMIZED_32) -c $< -o $@

$(BINDIR_OPTIMIZED_64)/%.o:%.c $(HEADERS_OPTIMIZED_64)
	$(CC) $(INCLUDES) $(CFLAGS_OPTIMIZED_64) -c $< -o $@

$(BINDIR_OPTIMIZED_64_ASM)/%.o:%.c $(HEADERS_OPTIMIZED_64_ASM)
	$(CC) $(INCLUDES) $(CFLAGS_OPTIMIZED_64_ASM) -c $< -o $@

$(BINDIR_OPTIMIZED_64_ASM)/%.o:%.s $(HEADERS_OPTIMIZED_64_ASM)
	$(CC) $(INCLUDES) -c $< -o $@

$(BINDIR_SIMPLE)/%.o:%.c $(HEADERS_SIMPLE)
	$(CC) $(INCLUDES) $(CFLAGS_SIMPLE) -c $< -o $@

$(BINDIR_SIMPLE32BI)/%.o:%.c $(HEADERS_SIMPLE32BI)
	$(CC) $(INCLUDES) $(CFLAGS_SIMPLE32BI) -c $< -o $@

$(BINDIR_INPLACE)/%.o:%.c $(HEADERS_INPLACE)
	$(CC) $(INCLUDES) $(CFLAGS_INPLACE) -c $< -o $@

$(BINDIR_INPLACE32BI)/%.o:%.c $(HEADERS_INPLACE32BI)
	$(CC) $(INCLUDES) $(CFLAGS_INPLACE32BI) -c $< -o $@

$(BINDIR_COMPACT)/%.o:%.c $(HEADERS_COMPACT)
	$(CC) $(INCLUDES) $(CFLAGS_COMPACT) -c $< -o $@

$(BINDIR_COMPACT8)/%.o:%.c $(HEADERS_COMPACT8)
	$(CC) $(INCLUDES) $(CFLAGS_COMPACT8) -c $< -o $@

.PHONY: KeccakReference KeccakReference32BI KeccakOptimized32 KeccakOptimized64 KeccakOptimized64asm KeccakSimple KeccakSimple32BI KeccakInplace KeccakInplace32BI KeccakCompact KeccakCompact8

KeccakReference: bin/KeccakReference

bin/KeccakReference:  $(BINDIR_REFERENCE) $(OBJECTS_REFERENCE)  $(HEADERS_REFERENCE)
	$(CC) $(CFLAGS_REFERENCE) -o $@ $(OBJECTS_REFERENCE)

KeccakReference32BI: bin/KeccakReference32BI

bin/KeccakReference32BI:  $(BINDIR_REFERENCE32BI) $(OBJECTS_REFERENCE32BI)  $(HEADERS_REFERENCE32BI)
	$(CC) $(CFLAGS_REFERENCE32BI) -o $@ $(OBJECTS_REFERENCE32BI)

KeccakOptimized32: bin/KeccakOptimized32

bin/KeccakOptimized32:  $(BINDIR_OPTIMIZED_32) $(OBJECTS_OPTIMIZED_32)  $(HEADERS_OPTIMIZED_32)
	$(CC) $(CFLAGS_OPTIMIZED_32) -o $@ $(OBJECTS_OPTIMIZED_32)

KeccakOptimized64: bin/KeccakOptimized64

bin/KeccakOptimized64:  $(BINDIR_OPTIMIZED_64) $(OBJECTS_OPTIMIZED_64)  $(HEADERS_OPTIMIZED_64)
	$(CC) $(CFLAGS_OPTIMIZED_64) -o $@ $(OBJECTS_OPTIMIZED_64)

KeccakOptimized64asm: bin/KeccakOptimized64asm

bin/KeccakOptimized64asm:  $(BINDIR_OPTIMIZED_64_ASM) $(OBJECTS_OPTIMIZED_64_ASM)  $(HEADERS_OPTIMIZED_64_ASM)
	$(CC) $(CFLAGS_OPTIMIZED_64_ASM) -o $@ $(OBJECTS_OPTIMIZED_64_ASM)

KeccakSimple: bin/KeccakSimple

bin/KeccakSimple:  $(BINDIR_SIMPLE) $(OBJECTS_SIMPLE)  $(HEADERS_SIMPLE)
	$(CC) $(CFLAGS_SIMPLE) -o $@ $(OBJECTS_SIMPLE)

KeccakSimple32BI: bin/KeccakSimple32BI

bin/KeccakSimple32BI:  $(BINDIR_SIMPLE32BI) $(OBJECTS_SIMPLE32BI)  $(HEADERS_SIMPLE32BI)
	$(CC) $(CFLAGS_SIMPLE32BI) -o $@ $(OBJECTS_SIMPLE32BI)

KeccakInplace: bin/KeccakInplace

bin/KeccakInplace:  $(BINDIR_INPLACE) $(OBJECTS_INPLACE)  $(HEADERS_INPLACE)
	$(CC) $(CFLAGS_INPLACE) -o $@ $(OBJECTS_INPLACE)

KeccakInplace32BI: bin/KeccakInplace32BI

bin/KeccakInplace32BI:  $(BINDIR_INPLACE32BI) $(OBJECTS_INPLACE32BI)  $(HEADERS_INPLACE32BI)
	$(CC) $(CFLAGS_INPLACE32BI) -o $@ $(OBJECTS_INPLACE32BI)

KeccakCompact: bin/KeccakCompact

bin/KeccakCompact:  $(BINDIR_COMPACT) $(OBJECTS_COMPACT)  $(HEADERS_COMPACT)
	$(CC) $(CFLAGS_COMPACT) -o $@ $(OBJECTS_COMPACT)

KeccakCompact8: bin/KeccakCompact8

bin/KeccakCompact8:  $(BINDIR_COMPACT8) $(OBJECTS_COMPACT8)  $(HEADERS_COMPACT8)
	$(CC) $(CFLAGS_COMPACT8) -o $@ $(OBJECTS_COMPACT8)

.PHONY: clean

clean:
	rm -rf bin/

.PHONY: eBASH

eBASH:
	cd eBASH ; python populate.py
