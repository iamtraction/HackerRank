#!/bin/python3

import os

# Complete the findDigits function below.
def findDigits(n):
    return len([i for i in map(int, list(str(n))) if i and n % i == 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
