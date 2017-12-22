#!/bin/env python3
import sys

line = sys.stdin.readline()[:-1]
hist = {}
for c in line:
    if c in hist:
        hist[c] += 1
    else:
        hist[c] = 1

for k, v in hist.items():
    print("{}: {}".format(k,v))
