#!/bin/env python3

import sys
import util

"""
Given: A protein string P.
Return: The total weight of P.
"""

protein_string = sys.stdin.readline()[:-1]
total_weight = 0
for acid in protein_string:
    total_weight += util.mass_of_amino_acid[acid]
print("{:.3f}".format(total_weight))
