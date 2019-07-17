#!/bin/python3

import os

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = [0]*6
    for t in arr: freq[t] += 1

    sorted_freq = sorted(enumerate(freq), key=lambda kv: (-kv[1], kv[0]))
    return sorted_freq[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
