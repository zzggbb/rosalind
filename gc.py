#!/bin/env python3

import sys
import util

"""
Given: At most 10 DNA strings in FASTA format.
Return: The ID of the string having the highest GC-content, followed by
the GC-content of that string.
"""

data = util.fasta(sys.stdin.readlines())
max_gc = -1
for k, v in data.items():
    gc = util.gc(v)
    if gc > max_gc:
        max_gc = gc
        max_id = k

print(max_id)
print("{:.6f}".format(max_gc * 100))
