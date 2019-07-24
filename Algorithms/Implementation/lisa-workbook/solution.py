#!/bin/python3

import math
import os

# Complete the workbook function below.
def workbook(n, k, arr):
    special_problems = 0

    page = 0
    for chapter in range(n):
        problems = []
        for p in range(math.ceil(arr[chapter] / k)):
            page += 1

            problems = list(filter(lambda x: x <= arr[chapter], range(p * k + 1, (p * k + 1 + k))))

            if page in problems:
                special_problems += 1

    return special_problems

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
