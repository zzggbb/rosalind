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

def codons(dna_string):
    for i in range(0, len(dna_string), 3):
        yield dna_string[i:i+3]

def gc(dna_string):
    count = 0
    for base in dna_string:
        if base == 'G' or base == 'C':
            count += 1
    return count / len(dna_string)

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

alphabet = 'ACGT'

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

mass_of_amino_acid = {
    'A':  71.03711,
    'C':  103.00919,
    'D':  115.02694,
    'E':  129.04259,
    'F':  147.06841,
    'G':  57.02146,
    'H':  137.05891,
    'I':  113.08406,
    'K':  128.09496,
    'L':  113.08406,
    'M':  131.04049,
    'N':  114.04293,
    'P':  97.05276,
    'Q':  128.05858,
    'R':  156.10111,
    'S':  87.03203,
    'T':  101.04768,
    'V':  99.06841,
    'W':  186.07931,
    'Y':  163.06333
}
