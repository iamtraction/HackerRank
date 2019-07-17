#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = -1

    i = 0
    while i < len(c):
        jumps += 1
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
