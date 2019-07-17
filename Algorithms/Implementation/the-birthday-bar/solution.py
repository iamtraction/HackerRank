#!/bin/python3

import os

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s) + 1 - m):
        if sum([s[i+j] for j in range(m)]) == d: count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
