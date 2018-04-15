#!/bin/env/python3

import sys
import util
import numpy

"""
Given: Three positive integers k, m, and n, representing a
population containing k+m+n organisms: k individuals are
homozygous dominant for a factor, m are heterozygous, and
n are homozygous recessive.

Return: The probability that two randomly selected mating
organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.

P(O(xy)) matrix:
- probability of a dominant phenotype offspring of parent x and y

   py 0    1    2
      k    m    n
px    -----------
0 k | 1    1    1
1 m | 1   .75  .5
2 n | 1   .5    0

P(xy) matrix:
- probability of randomly selecting parents x and y
- note that this must be divided by t * (t-1)

   py 0       1     2
      k       m     n
px    ------------------
0 k | k^2-k   km    kn
1 m |  mk   m^2-m   mn
2 n |  nk     nm   n^2-n

P(xy) * P(O(xy)):
- The probability that two randomly selected mating organisms
  will produce an individual displaying the dominant phenotype
  is the dot product of `poxy` and `pxy`
"""

k, m, n = numpy.loadtxt(sys.stdin)
t = k + m + n
poxy = [1, 1, 1, 1, 3/4, 0.5, 1, 0.5, 0]
pxy = [k**2 - k, k*m, k*n, m*k, m**2-m, m*n, n*k, n*m, n**2-n]
ret = numpy.dot(poxy, pxy) / (t**2 - t)
print(ret)
