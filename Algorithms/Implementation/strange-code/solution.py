#!/bin/python3

import os

# Complete the strangeCounter function below.
def strangeCounter(t):
    value = 3
    while t > value:
        t = t - value
        value *= 2
    return value - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
