#!/bin/python3

import os

# Complete the fairRations function below.
def fairRations(B):
    carry = 0
    carries = 0

    for b in B:
        carry = (carry + b) & 1
        carries += carry

    return "NO" if carry else carries * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
