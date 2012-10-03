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

/************** Timing routine (for performance measurements) ***********/
/* By Doug Whiting */
/* unfortunately, this is generally assembly code and not very portable */
#if defined(_M_IX86) || defined(__i386) || defined(_i386) || defined(__i386__) || defined(i386) || \
    defined(_X86_)   || defined(__x86_64__) || defined(_M_X64) || defined(__x86_64)
#define _Is_X86_    1
#endif

#if  defined(_Is_X86_) && (!defined(__STRICT_ANSI__)) && (defined(__GNUC__) || !defined(__STDC__)) && \
    (defined(__BORLANDC__) || defined(_MSC_VER) || defined(__MINGW_H) || defined(__GNUC__))
#define HI_RES_CLK_OK         1          /* it's ok to use RDTSC opcode */

#if defined(_MSC_VER) // && defined(_M_X64)
#include <intrin.h>
#pragma intrinsic(__rdtsc)         /* use MSVC rdtsc call where defined */
#endif

#endif

typedef unsigned int uint_32t;

uint_32t HiResTime(void)           /* return the current value of time stamp counter */
    {
#if defined(HI_RES_CLK_OK)
    uint_32t x[2];
#if   defined(__BORLANDC__)
#define COMPILER_ID "BCC"
    __emit__(0x0F,0x31);           /* RDTSC instruction */
    _asm { mov x[0],eax };
#elif defined(_MSC_VER)
#define COMPILER_ID "MSC"
#if defined(_MSC_VER) // && defined(_M_X64)
    x[0] = (uint_32t) __rdtsc();
#else
    _asm { _emit 0fh }; _asm { _emit 031h };
    _asm { mov x[0],eax };
#endif
#elif defined(__MINGW_H) || defined(__GNUC__)
#define COMPILER_ID "GCC"
    asm volatile("rdtsc" : "=a"(x[0]), "=d"(x[1]));
#else
#error  "HI_RES_CLK_OK -- but no assembler code for this platform (?)"
#endif
    return x[0];
#else
    /* avoid annoying MSVC 9.0 compiler warning #4720 in ANSI mode! */
#if (!defined(_MSC_VER)) || (!defined(__STDC__)) || (_MSC_VER < 1300)
    FatalError("No support for RDTSC on this CPU platform\n");
#endif
    return 0;
#endif /* defined(HI_RES_CLK_OK) */
    }

#define TIMER_SAMPLE_CNT (10)

uint_32t calibrate()
{
    uint_32t dtMin = 0xFFFFFFFF;        /* big number to start */
    uint_32t t0,t1,i;

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        t1 = HiResTime();
        if (dtMin > t1-t0)              /* keep only the minimum time */
            dtMin = t1-t0;
        }
    return dtMin;
}

#include "DoublePermutation.h"

uint_32t measureDoubleKeccakAbsorb1344bits(uint_32t dtMin)
{
    uint_32t tMin = 0xFFFFFFFF;         /* big number to start */
    uint_32t t0,t1,i;
    ALIGN unsigned char state[KeccakPermutationSizeInBytes*2];
    ALIGN unsigned char input[168*2];

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        KeccakDoublePermutationOnWordsAfterXoring2x1344bits((V128*)state, (V128*)input);
        t1 = HiResTime();
        if (tMin > t1-t0 - dtMin)       /* keep only the minimum time */
            tMin = t1-t0 - dtMin;
        }

    /* now tMin = # clocks required for running RoutineToBeTimed() */
    
    return tMin;
}

uint_32t measureDoubleKeccakAbsorb1088bits(uint_32t dtMin)
{
    uint_32t tMin = 0xFFFFFFFF;         /* big number to start */
    uint_32t t0,t1,i;
    ALIGN unsigned char state[KeccakPermutationSizeInBytes*2];
    ALIGN unsigned char input[136*2];

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        KeccakDoublePermutationOnWordsAfterXoring2x1088bits((V128*)state, (V128*)input);
        t1 = HiResTime();
        if (tMin > t1-t0 - dtMin)       /* keep only the minimum time */
            tMin = t1-t0 - dtMin;
        }

    /* now tMin = # clocks required for running RoutineToBeTimed() */
    
    return tMin;
}

uint_32t measureDoubleKeccakAbsorb1024bits(uint_32t dtMin)
{
    uint_32t tMin = 0xFFFFFFFF;         /* big number to start */
    uint_32t t0,t1,i;
    ALIGN unsigned char state[KeccakPermutationSizeInBytes*2];
    ALIGN unsigned char input[128*2];

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        KeccakDoublePermutationOnWordsAfterXoring2x1024bits((V128*)state, (V128*)input);
        t1 = HiResTime();
        if (tMin > t1-t0 - dtMin)       /* keep only the minimum time */
            tMin = t1-t0 - dtMin;
        }

    /* now tMin = # clocks required for running RoutineToBeTimed() */
    
    return tMin;
}

uint_32t measureDoubleKeccakAbsorb512bits(uint_32t dtMin)
{
    uint_32t tMin = 0xFFFFFFFF;         /* big number to start */
    uint_32t t0,t1,i;
    ALIGN unsigned char state[KeccakPermutationSizeInBytes*2];
    ALIGN unsigned char input[64*2];

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        KeccakDoublePermutationOnWordsAfterXoring2x512bits((V128*)state, (V128*)input);
        t1 = HiResTime();
        if (tMin > t1-t0 - dtMin)       /* keep only the minimum time */
            tMin = t1-t0 - dtMin;
        }

    /* now tMin = # clocks required for running RoutineToBeTimed() */
    
    return tMin;
}

uint_32t measureDoubleKeccakPermutation(uint_32t dtMin)
{
    uint_32t tMin = 0xFFFFFFFF;         /* big number to start */
    uint_32t t0,t1,i;
    ALIGN unsigned char state[KeccakPermutationSizeInBytes*2];

    for (i=0;i < TIMER_SAMPLE_CNT;i++)  /* calibrate the overhead for measuring time */
        {
        t0 = HiResTime();
        KeccakDoublePermutationOnWords((V128*)state);
        t1 = HiResTime();
        if (tMin > t1-t0 - dtMin)       /* keep only the minimum time */
            tMin = t1-t0 - dtMin;
        }

    /* now tMin = # clocks required for running RoutineToBeTimed() */
    
    return tMin;
}



void doTiming()
{
    uint_32t calibration;
    uint_32t measurementDoubleKeccakPermutation;
    uint_32t measurementDoubleKeccakAbsorb1344bits;
    uint_32t measurementDoubleKeccakAbsorb1088bits;
    uint_32t measurementDoubleKeccakAbsorb1024bits;

    calibration = calibrate();

    measurementDoubleKeccakPermutation = measureDoubleKeccakPermutation(calibration);
    printf("Cycles for DoubleKeccakPermutation(state): %d\n", measurementDoubleKeccakPermutation);
    printf("Cycles per byte for rate 1024: %f\n", measurementDoubleKeccakPermutation/128.0/2.0);
    printf("Cycles per byte for rate 1088: %f\n", measurementDoubleKeccakPermutation/136.0/2.0);
    printf("Cycles per byte for rate 1344: %f\n", measurementDoubleKeccakPermutation/168.0/2.0);
    printf("\n");

    measurementDoubleKeccakAbsorb1344bits = measureDoubleKeccakAbsorb1344bits(calibration);
    printf("Cycles for DoubleKeccakAbsorb1344bits(state, input): %d\n", measurementDoubleKeccakAbsorb1344bits);
    printf("Cycles per byte for rate 1344: %f\n", measurementDoubleKeccakAbsorb1344bits/168.0/2.0);
    printf("\n");

    measurementDoubleKeccakAbsorb1088bits = measureDoubleKeccakAbsorb1088bits(calibration);
    printf("Cycles for DoubleKeccakAbsorb1088bits(state, input): %d\n", measurementDoubleKeccakAbsorb1088bits);
    printf("Cycles per byte for rate 1088: %f\n", measurementDoubleKeccakAbsorb1088bits/136.0/2.0);
    printf("\n");

    measurementDoubleKeccakAbsorb1024bits = measureDoubleKeccakAbsorb1024bits(calibration);
    printf("Cycles for DoubleKeccakAbsorb1024bits(state, input): %d\n", measurementDoubleKeccakAbsorb1024bits);
    printf("Cycles per byte for rate 1024: %f\n", measurementDoubleKeccakAbsorb1024bits/128.0/2.0);
    printf("\n");
}
