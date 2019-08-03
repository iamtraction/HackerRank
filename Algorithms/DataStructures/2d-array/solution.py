#!/bin/python3

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = None
    for i in range(len(arr) - 2):
        curr_sum = 0
        for j in range(len(arr[i]) - 2):
            curr_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            max_sum = curr_sum if max_sum == None else (curr_sum if curr_sum > max_sum else max_sum)

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
