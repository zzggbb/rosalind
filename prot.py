#!/bin/env python3

import sys
import util

"""
Given: An RNA string 's' corresponding to a strand of mRNA
Return: The protein string encoded by 's'.
"""

def protein_string(rna_string):
    amino_acids = []
    codons = util.codons(rna_string)

    while next(codons) != 'AUG':
        pass

    amino_acids.append('M')
    for codon in codons:
        amino_acid = util.amino_acid_of_codon[codon]
        if amino_acid == '$':
            break
        amino_acids.append(amino_acid)

    return ''.join(amino_acids)

if __name__ == '__main__':
    rna_string = sys.stdin.readline()[:-1]
    print(protein_string(rna_string))
