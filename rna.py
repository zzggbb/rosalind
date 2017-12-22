#!/bin/env python3
import sys

line = sys.stdin.readlines()[0][:-1]
out = line.replace('T', 'U')
print(out)
