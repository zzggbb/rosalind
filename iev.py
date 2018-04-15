#!/bin/env python3

import sys
import numpy

"""
Given: The six given positive integers represent the number of couples having
       the following genotypes:
           1. AA-AA
           2. AA-Aa
           3. AA-aa
           4. Aa-Aa
           5. Aa-aa
           6. aa-aa
Return: The expected number of offspring displaying the dominant phenotype in
        the next generation, under the assumption that every couple has
        exactly two offspring.

Punnett Squares:
        A  A    A  a    a  a
      A AA AA   AA Aa   Aa Aa
      A AA AA   AA Aa   Aa Aa
      1         1       1
      A AA AA   AA Aa   Aa Aa
      a Aa Aa   Aa aa   aa aa
      1         3/4     1/2
      a Aa Aa   Aa aa   aa aa
      a Aa Aa   Aa aa   aa aa
      1         1/2     0
"""

# f(a b c d e f) = 2a + 2b + 2c + 3d/2 + e
couples_per_genotype = numpy.loadtxt(sys.stdin)
num_offspring = numpy.sum(couples_per_genotype * [2, 2, 2, 1.5, 1, 0])
print(num_offspring)
