#!/bin/python3

import os

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    chocos = n // c
    return chocos + (chocos - 1) // (m - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
