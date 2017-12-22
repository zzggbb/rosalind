#!/bin/env python3
import sys
from util import fasta

strings = list(fasta(sys.stdin.readlines()).values())
print(strings)
