#!/usr/bin/env python
# Pentagonal numbers are generated by the formula, 
# P(n)=n(3n-1)/2. The first ten pentagonal numbers are:
# 
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# 
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. 
# However, their difference, 70  22 = 48, is not 
# pentagonal.
# 
# Find the pair of pentagonal numbers, Pj and Pk, 
# for which their sum and difference is pentagonal 
# and D = |Pk - Pj| is minimised; what is the value of D?
from itertools import *
from math import *
from operator import *

def pentagonal(n):
    return n*(3*n-1)/2

def main():
    pentagonals = set(pentagonal(n) for n in range(1, 3000))
    c = combinations(pentagonals, 2)
    for p in c:
        if add(*p) in pentagonals and abs(sub(*p)) in pentagonals:
            print p, abs(sub(*p))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')

