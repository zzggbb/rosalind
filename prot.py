#!/bin/env python3

import sys
import util

"""
Given: An RNA string 's' corresponding to a strand of mRNA
Return: The protein string encoded by 's'.
"""

rna_string = sys.stdin.readline()[:-1]
codons = util.codons(rna_string)
protein = util.protein(codons)
print(''.join(protein))
