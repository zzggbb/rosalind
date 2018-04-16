#!/bin/env python3

import sys
import util

"""
Given: A DNA string 't'
Return: The transcribed RNA string of 't'.
"""

dna_string = sys.stdin.readline()[:-1]
rna_string = util.rna(dna_string)
print(rna_string)
