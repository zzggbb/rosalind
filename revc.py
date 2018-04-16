#!/bin/env python3

import sys
import util

"""
Given: A DNA string s.
Return: The reverse complement of s.
"""

dna_string = sys.stdin.readline()[:-1]
reverse_complement = ''.join(util.revc(dna_string))
print(reverse_complement)
