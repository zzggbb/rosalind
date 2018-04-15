#!/bin/env python3

import sys
import util

dna_string = sys.stdin.readline()[:-1]
reverse_complement = ""
for i in range(len(dna_string) - 1, -1, -1):
    reverse_complement += util.complement_of_base[dna_string[i]]
print(reverse_complement)
