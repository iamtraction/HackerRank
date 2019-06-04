#!/bin/python3

import os

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes = [ 5 // 2 ]

    for i in range(n - 1):
        likes.append(likes[i] * 3 // 2)

    return sum(likes)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
