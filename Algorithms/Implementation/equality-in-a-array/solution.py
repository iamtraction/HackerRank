#!/bin/python3

import os

# Complete the equalizeArray function below.
def equalizeArray(arr):
    freq = {}
    for el in arr:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1

    return len(arr) - max(freq.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
