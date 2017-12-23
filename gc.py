#!/bin/env python3

import sys
import util

"""
Given: At most 10 DNA strings in FASTA format.
Return: The ID of the string having the highest GC-content, followed by
the GC-content of that string.
"""

data = util.fasta(sys.stdin.readlines())
