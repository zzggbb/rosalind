#!/bin/env python3
import sys

dna_string = sys.stdin.readline()[:-1]
map = {
    'C':'G',
    'G':'C',
    'A':'T',
    'T':'A'
}
complement = [map[base] for base in dna_string]
reverse = complement[::-1]
print(''.join(reverse))
