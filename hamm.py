#!/bin/env python3

import sys

"""
Given: Two DNA strings 's' and 't' of equal length.
Return: The Hamming distance dH(s,t).
"""

s = sys.stdin.readline()[:-1]
t = sys.stdin.readline()[:-1]

assert len(s) == len(t)

diff = 0
for i in range(len(s)):
    if s[i] != t[i]:
        diff += 1
print(diff)
