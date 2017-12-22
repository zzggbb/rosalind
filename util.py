#!/bin/env python3

def fasta(lines):
    data = {}
    for line in lines:
        if line[0] == '>':
            label = line[1:-1]
            data[label] = ""
        else:
            data[label] += line[:-1]
    return data

def codons(s):
    for i in range(0, len(s), 3):
        yield s[i:i+3]

def gc(s):
    count = 0
    for c in s:
        if c == 'G' or c == 'C':
            count += 1
    return count / len(s)


codon_to_amino_acid = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F',
    'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L',
    'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M',
    'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S',
    'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P',
    'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N',
    'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': '$', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '$',
    'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R',
    'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S',
    'GGC': 'G', 'UGA': '$', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}
