#!/bin/python3

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    return int(sum((ar.count(i) - ar.count(i) % 2) / 2 for i in set(ar)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
