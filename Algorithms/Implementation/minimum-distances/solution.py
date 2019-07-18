#!/bin/python3

import os

# Complete the minimumDistances function below.
def minimumDistances(a):
    pairs = set([i for i in a if a.count(i) > 1])
    distances = []

    for i in pairs:
        start = a.index(i)
        distances.append(a.index(i, start + 1) - start)

    return min(distances) if len(distances) else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
