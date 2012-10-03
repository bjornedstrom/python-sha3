/*
The Keccak sponge function, designed by Guido Bertoni, Joan Daemen,
Michaël Peeters and Gilles Van Assche. For more information, feedback or
questions, please refer to our website: http://keccak.noekeon.org/

Implementation by the designers,
hereby denoted as "the implementer".

To the extent possible under law, the implementer has waived all copyright
and related or neighboring rights to the source code in this file.
http://creativecommons.org/publicdomain/zero/1.0/
*/

#include <stdio.h>
#include <string.h>

#ifdef D2
#include "timing-Double.h"
#include "DoublePermutation.h"
#endif

#ifdef D4
#include "timing-Quad.h"
#include "QuadPermutation.h"
#endif

#if defined(c256) && defined(D2)
#include "Keccakc256TreeD2.h"
#endif
#if defined(c512) && defined(D2)
#include "Keccakc512TreeD2.h"
#endif


#ifdef D2
typedef unsigned long long int UINT64;

void printDoubleState(const UINT64* doubleState)
{
    unsigned int i;
    for(i=0; i<25; i++) {
        printf("%08X", (doubleState[i*2] >> 32));
        printf("%08X", (doubleState[i*2] & 0xFFFFFFFFULL));
        if ((i%5) == 4)
            printf("\n");
        else
            printf(" ");
    }

    printf("\n");

    for(i=0; i<25; i++) {
        printf("%08X", (doubleState[i*2+1] >> 32));
        printf("%08X", (doubleState[i*2+1] & 0xFFFFFFFFULL));
        if ((i%5) == 4)
            printf("\n");
        else
            printf(" ");
    }
}

void testDoublePermutation()
{
    unsigned int i;
    ALIGN UINT64 doubleState[25*2];
    memset(doubleState, 0, sizeof(doubleState));
    printf("Double state before:\n");
    printDoubleState(doubleState);
    KeccakDoublePermutationOnWords((V128*)doubleState);
    printf("Double state after:\n");
    printDoubleState(doubleState);

    for(i=0; i<25; i++)
        doubleState[i*2] = 0;

    KeccakDoublePermutationOnWords((V128*)doubleState);
    printf("Double state after after:\n");
    printDoubleState(doubleState);
}
#endif

#ifdef rateInBytes
void testKeccakTree()
{
    unsigned char message[1000];
    unsigned char out[1000];
    unsigned int len;
    unsigned int i;
    
    for(len=0; len<=1000; len++) {
        for(i=0; i<len; i++)
            message[i] = (unsigned char)(len-i);
        crypto_hash(out, message, len);
        printf("Message of length %d bits\n", len*8);
        for(i=0; i<rateInBytes; i++)
            printf("%02x ", out[i]);
        printf("\n");
    }
}
#endif

int main()
{
#ifdef D2
    //testDoublePermutation();
#endif
#ifdef rateInBytes
    testKeccakTree();
#endif
    doTiming();
    return 0;
}
