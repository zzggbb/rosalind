#!/bin/env python3

import sys
import util

"""
Given: A DNA string 's'
Return: Four integers (separated by spaces) counting the respective
number of times that the symbols 'A', 'C', 'G', and 'T' occur in 's'.
"""

dna_string = sys.stdin.readline()[:-1]
base_counter = {}
for base in dna_string:
    if base in base_counter:
        base_counter[base] += 1
    else:
        base_counter[base] = 1

print(' '.join(
    str(base_counter[base]) for base in util.alphabet
))
