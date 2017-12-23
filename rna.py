#!/bin/env python3

import sys

"""
Given: A DNA string 't'
Return: The transcribed RNA string of 't'.
"""

dna_string = sys.stdin.readline()[:-1]
rna_string = dna_string.replace('T', 'U')
print(rna_string)
