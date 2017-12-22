#!/bin/env python3
import sys

s = sys.stdin.readline()[:-1]
t = sys.stdin.readline()[:-1]

indexes = []
for i in range(len(s)):
    j = 0
    while i+j < len(s) and j < len(t) and s[i+j] == t[j]:
        j += 1
    if j == len(t):
        indexes.append(i + 1)

print(' '.join(str(d) for d in indexes))
