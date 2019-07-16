#!/bin/python3

import math
import os

# Complete the squares function below.
def squares(a, b):
    count = 0

    i = a
    while i <= b:
        sqrt = math.sqrt(i)
        if sqrt.is_integer():
            count += 1
            i = int((sqrt + 1) * (sqrt + 1))
        else:
            i += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
