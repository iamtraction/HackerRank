#!/bin/python3

import os

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    sticks_cut = []

    while len(arr):
        sticks_cut.append(len(arr))
        arr = list(filter(lambda x: x != min(arr), arr))

    return sticks_cut

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
