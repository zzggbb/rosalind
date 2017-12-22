#!/bin/env python3
import sys
import util

s = sys.stdin.readline()[:-1]

assert len(s) % 3 == 0

amino_acids = []
codons = util.codons(s)

while next(codons) != 'AUG':
    pass

amino_acids.append('M')
for codon in codons:
    amino_acid = util.codon_to_amino_acid[codon]
    if amino_acid == '$':
        break
    amino_acids.append(amino_acid)

print(''.join(amino_acids))
