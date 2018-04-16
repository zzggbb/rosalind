#!/bin/env python3

import sys
import util

"""
Given: A protein string.
Return: The total number of different RNA strings from which the protein could
        have been translated, modulo 1,000,000.
"""

n = 3 # always 3 possible stop codons
protein_string = sys.stdin.readline()[:-1]
for acid in protein_string:
    n *= util.codons_per_amino_acid[acid]

print(n % 10**6)
