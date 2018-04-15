#!/bin/env python3

import sys
import numpy
import util

index_of_base = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

dna_strings = list(util.fasta(sys.stdin.readlines()).values())
m = len(dna_strings)
n = len(dna_strings[0])

profile = numpy.zeros((4, n), dtype=numpy.int8)
consensus = ''

for column in range(n):
    for row in range(m):
        base = dna_strings[row][column]
        profile[index_of_base[base]][column] += 1

    max_count = -1
    max_base = 'A'
    for i in range(4):
        count = profile[i][column]
        if count > max_count:
            max_count = count
            max_base = util.alphabet[i]

    consensus += max_base

print(consensus)
for i in range(4):
    base = util.alphabet[i]
    row = ' '.join(str(count) for count in profile[i])
    print("{}: {}".format(base, row))
