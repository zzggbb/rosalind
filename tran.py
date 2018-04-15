#!/bin/env python3

import sys
import util

s1, s2 = util.fasta(sys.stdin.readlines()).values()

assert len(s1) == len(s2)

n = len(s1)

transitions = 0
transversions = 0
for i in range(n):
    c1 = s1[i]
    c2 = s2[i]
    if c1 == c2:
        continue
    # ord('A') + ord('G') = 136
    # ord('C') + ord('T') = 151
    if ord(c1) + ord(c2) in [136, 151]:
        transitions += 1
    else:
        transversions += 1

print("{:.11f}".format(transitions/transversions))
