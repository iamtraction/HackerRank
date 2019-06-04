#!/bin/python3

import os

# Complete the utopianTree function below.
def utopianTree(n):
    height = 0
    for i in range(n + 1):
        height = height * 2 if i & 1 else height + 1
    return height

def utopianTree_2(n):
    return ~(~1 << (n >> 1)) << n % 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
