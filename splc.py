#!/bin/env python3

import sys
import util

"""
Given: A DNA string 's' and a collection of substrings of 's' acting
as introns.  All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating
the exons of 's'.
"""

data = list(util.fasta(sys.stdin.readlines()).values())
dna_string = data[0]
introns = data[1:]
for intron in introns:
    dna_string = dna_string.replace(intron, '')

rna_string = util.rna(dna_string)
codons = util.codons(rna_string)
protein = util.protein(codons)
print(''.join(protein))
