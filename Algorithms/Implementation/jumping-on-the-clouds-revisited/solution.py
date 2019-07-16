#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    return 100 - sum(1 + 2 * c[i] for i in range(0, len(c), k))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
