#!/bin/env python3

import sys
import util

"""
Given: An RNA string 's' corresponding to a strand of mRNA
Return: The protein string encoded by 's'.
"""

dna_string = sys.stdin.readline()[:-1]

assert len(dna_string) % 3 == 0

amino_acids = []
codons = util.codons(dna_string)

while next(codons) != 'AUG':
    pass

amino_acids.append('M')
for codon in codons:
    amino_acid = util.codon_to_amino_acid[codon]
    if amino_acid == '$':
        break
    amino_acids.append(amino_acid)

print(''.join(amino_acids))
