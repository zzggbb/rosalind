#!/bin/env python3

import sys
import util

"""
Given: A DNA string in FASTA format.
Return: The position and length of every reverse palindrome in the
string having length between 4 and 12.
"""

MIN_LEN = 4
MAX_LEN = 12

dna_string = list(util.fasta(sys.stdin.readlines()).values())[0]
dna_len = len(dna_string)

for i in range(0, dna_len - MIN_LEN + 1):
    search_space = dna_len - i
    current_max_len = min(MAX_LEN, search_space)
    for l in range(MIN_LEN, current_max_len + 1):
        if util.reverse_palindrome(dna_string, i, i + l - 1):
            print("{} {}".format(i + 1, l))
