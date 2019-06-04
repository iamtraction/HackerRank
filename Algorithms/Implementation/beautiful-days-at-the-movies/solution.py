#!/bin/python3

import os

def reverse(n):
    return int(str(n)[::-1])

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_days = [ d for d in range(i, j + 1) if abs(d - reverse(d)) % k == 0 ]
    return len(beautiful_days)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
