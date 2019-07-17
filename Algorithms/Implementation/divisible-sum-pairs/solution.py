#!/bin/python3

import os

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    bucket = [0] * k
    pairs = 0
    for el in ar:
        modval = el % k
        pairs += bucket[(k - modval) % k]
        bucket[modval] += 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
