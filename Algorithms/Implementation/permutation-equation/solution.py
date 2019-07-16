#!/bin/python3

import os

# Complete the permutationEquation function below.
def permutationEquation(p):
    p_inverse = [0] * len(p)
    i = 0
    for e in p:
        p_inverse[e - 1] = i = i + 1

    return [p_inverse[p_inverse[i] - 1] for i in range(n)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
