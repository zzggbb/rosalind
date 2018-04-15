#!/bin/env python3

import sys
import util
import numpy

"""
Given: Positive integers n and k.
Return: The total number of rabbit pairs that will be present after 'n'
months, if we begin with 1 pair and in each generation, every pair of
reproduction-age rabbits produces a litter of 'k' rabbit pairs.
"""

@util.memoize
def rabbits(k, month):
    if month == 0:
        return 0
    if month == 1:
        return 1
    return k * rabbits(k, month - 2) + rabbits(k, month - 1)

n, k = numpy.loadtxt(sys.stdin)
print(rabbits(k, n))
