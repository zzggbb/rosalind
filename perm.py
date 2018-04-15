#!/bin/env python3

import sys
import util

"""
Given: A positive integer 'n'.
Return: The total number of permutations of length 'n', followed by a list
of all such permutations, in any order
"""

n = int(sys.stdin.read(1))
set = list(range(1,n+1))
permutations = list(util.permute(set))
print(len(permutations))
for perm in permutations:
    print(' '.join(str(i) for i in perm))
