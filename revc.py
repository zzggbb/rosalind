#!/bin/env python3
import sys

line = sys.stdin.readline()[:-1]
map = {
    'C':'G',
    'G':'C',
    'A':'T',
    'T':'A'
}
complement = [map[c] for c in line]

reverse = complement[::-1]
print(''.join(reverse))
