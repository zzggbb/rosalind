#!/bin/env python3

N_CODON = 3
alphabet = 'ACGT'

def revc(string):
    for base in string[::-1]:
        yield complement_of_base[base]

def rna(dna_string):
    return dna_string.replace('T', 'U')

def fasta(lines):
    data = {}
    for line in lines:
        if line[0] == '>':
            label = line[1:-1]
            data[label] = ""
        else:
            data[label] += line[:-1]
    return data

def codons(string):
    length = len(string)
    num_codons = length - (length % N_CODON)
    for i in range(0, num_codons, N_CODON):
        yield string[i:i+N_CODON]

def frames(string):
    for i in range(N_CODON):
        yield codons(string[i:])

def gc(string):
    count = 0
    for base in string:
        if base == 'G' or base == 'C':
            count += 1
    return count / len(string)

def protein(codons):
    while next(codons) != 'AUG':
        pass

    yield 'M'
    for codon in codons:
        acid = amino_acid_of_codon[codon]
        if acid == '$':
            break
        yield acid

def permute(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permute(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def reverse_palindrome(string, i, j):
    while i <= j:
        if string[i] != complement_of_base[string[j]]:
            return False
        i += 1
        j -= 1

    return True

def memoize(f):
    previous = {}
    def g(*args):
        if args in previous:
            return previous[args]
        previous[args] = f(*args)
        return previous[args]

    return g


complement_of_base = {
    'C': 'G',
    'G': 'C',
    'A': 'T',
    'T': 'A'
}

amino_acid_of_codon = {
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

codons_of_amino_acid = {
    '$': ['UAA', 'UAG', 'UGA'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGU', 'UGC'],
    'D': ['GAU', 'GAC'],
    'F': ['UUU', 'UUC'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'], 'E': ['GAA', 'GAG'],
    'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
    'M': ['AUG'],
    'N': ['AAU', 'AAC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
}

codons_per_amino_acid = {
    '$': 3, 'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4,
    'V': 4, 'W': 1, 'Y': 2,
}

mass_of_amino_acid = {
    'A':  71.03711,  'C':  103.00919, 'D':  115.02694, 'E':  129.04259,
    'F':  147.06841, 'G':  57.02146,  'H':  137.05891, 'I':  113.08406,
    'K':  128.09496, 'L':  113.08406, 'M':  131.04049, 'N':  114.04293,
    'P':  97.05276,  'Q':  128.05858, 'R':  156.10111, 'S':  87.03203,
    'T':  101.04768, 'V':  99.06841,  'W':  186.07931, 'Y':  163.06333
}
