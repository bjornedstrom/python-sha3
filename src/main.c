#include "KeccakHash.h"

#include <stdio.h>

int main()
{
	unsigned char output[512];
	int i;

	Keccak_HashInstance inst;
	Keccak_HashInitialize_SHAKE128(&inst);

	Keccak_HashUpdate(&inst, "The quick brown fox jumps over the lazy dog", 43*8);

	Keccak_HashFinal(&inst, output);
	Keccak_HashSqueeze(&inst, output, 256);

	for (i = 0; i < 256/8; i++) {
		printf("%02x", output[i]);
	}
	printf("\n");

	return 0;
}
