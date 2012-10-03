all: Keccakc256TreeD2 Keccakc512TreeD2

SOURCES_D2 = \
    Sources/mainOptimized.c \
    Sources/timing-Double.c \
    Sources/DoublePermutation.c

HEADERS_D2 = \
    Sources/timing-Double.h \
    Sources/KeccakF-1600-unrolling.macros \
    Sources/DoublePermutation.h

SOURCES_c256D2 = $(SOURCES_D2) \
    Sources/Keccakc256TreeD2.c

SOURCES_c512D2 = $(SOURCES_D2) \
    Sources/Keccakc512TreeD2.c

HEADERS_c256D2 = $(HEADERS_D2) \
    Sources/Keccakc256TreeD2.h

HEADERS_c512D2 = $(HEADERS_D2) \
    Sources/Keccakc512TreeD2.h

BINDIR_c256D2 = bin/c256D2

$(BINDIR_c256D2):
	mkdir -p $(BINDIR_c256D2)

OBJECTS_c256D2 = $(addprefix $(BINDIR_c256D2)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_c256D2))))

CFLAGS_c256D2 = -Dc256 -DD2 -fomit-frame-pointer -O3 -g0 -march=native -mtune=native

BINDIR_c512D2 = bin/c512D2

$(BINDIR_c512D2):
	mkdir -p $(BINDIR_c512D2)

OBJECTS_c512D2 = $(addprefix $(BINDIR_c512D2)/, $(notdir $(patsubst %.c,%.o,$(SOURCES_c512D2))))

CFLAGS_c512D2 = -Dc512 -DD2 -fomit-frame-pointer -O3 -g0 -march=native -mtune=native

VPATH = Sources

INCLUDES = -ISources

$(BINDIR_c256D2)/%.o:%.c $(HEADERS_c256D2)
	$(CC) $(INCLUDES) $(CFLAGS_c256D2) -c $< -o $@

$(BINDIR_c512D2)/%.o:%.c $(HEADERS_c512D2)
	$(CC) $(INCLUDES) $(CFLAGS_c512D2) -c $< -o $@

.PHONY: Keccakc256TreeD2 Keccakc512TreeD2

Keccakc256TreeD2: bin/Keccakc256TreeD2

bin/Keccakc256TreeD2:  $(BINDIR_c256D2) $(OBJECTS_c256D2)  $(HEADERS_c256D2)
	$(CC) $(CFLAGS_c256D2) -o $@ $(OBJECTS_c256D2)

Keccakc512TreeD2: bin/Keccakc512TreeD2

bin/Keccakc512TreeD2:  $(BINDIR_c512D2) $(OBJECTS_c512D2)  $(HEADERS_c512D2)
	$(CC) $(CFLAGS_c512D2) -o $@ $(OBJECTS_c512D2)

.PHONY: clean

clean:
	rm -rf bin/
