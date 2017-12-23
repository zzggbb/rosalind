#!/bin/env python3

import sys
from util import fasta

"""
Given: A collection of 'k' DNA strings each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

strings = list(fasta(sys.stdin.readlines()).values())
print(strings)
