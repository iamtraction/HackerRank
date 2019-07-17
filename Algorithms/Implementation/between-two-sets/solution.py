#!/bin/python3

import os
import math
from functools import reduce

def lcm(a, b):
    a = int(a)
    b = int(b)
    return abs(a) / math.gcd(a, b) * abs(b)

def list_gcd(arr):
    return reduce(math.gcd, arr)

def list_lcm(arr):
    return reduce(lcm, arr, 1)

def divisors(n, m):
    if m == 1: return [1]
    if n % m == 0: return [m] + divisors(n, m - 1)
    return divisors(n, m - 1)

# Complete the getTotalX function below.
def getTotalX(a, b):
    # Write your code here.
    magic_number = int(list_gcd(b)) / int(list_lcm(a))
    if int(magic_number) < magic_number:
        return 0
    return len(divisors(magic_number, magic_number))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
