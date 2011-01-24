#!/usr/bin/env python
# The sequence of triangle numbers is generated by adding 
# the natural numbers. So the 7^(th) triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#      10: 1,2,5,10
#      15: 1,3,5,15
#      21: 1,3,7,21
#      28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over
# five divisors. What is the value of the first triangle number
# to have over five hundred divisors?
import math
from collections import defaultdict

def factorize(n):
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

_triangle_cache = {1: 1}
def triangle(n):
    if n < 1:
        return 0
    try:
        return _triangle_cache[n]
    except KeyError:
        result = n + triangle(n-1)
        _triangle_cache[n] = result
        return result

def num_divisors(n):
    factors = sorted(factorize(n))
    histogram = defaultdict(int)
    for factor in factors:
        histogram[factor] += 1
    # number of divisors is equal to product of 
    # incremented exponents of prime factors
    from operator import mul
    try:
        return reduce(mul, [exponent + 1 for exponent in histogram.values()])
    except:
        return 1

triangles = (triangle(i) for i in range(1,100000))
divisible_triangles = (i for i in triangles if num_divisors(i) > 500)
for n in divisible_triangles:
    print n
    break
