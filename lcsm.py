#!/bin/env python3

import sys
from util import fasta

"""
Given: A collection of 'k' DNA strings each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Notes:
Start with the longest candidates, and work towards shorter ones.
Once a candidate is a solution, the search is done.
Need a way of knowing if a given substring exists in a given string.
"""

strings = list(fasta(sys.stdin.readlines()).values())
print(strings)
