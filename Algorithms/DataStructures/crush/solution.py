#!/bin/python3

import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
        
    for query in queries:
        arr[query[0] - 1] += query[2]
        arr[query[1]] -= query[2]
    
    sum = 0
    max_num = 0
    for i in range(n):
        sum += arr[i]
        max_num = max(max_num, sum)
    
    return max_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
