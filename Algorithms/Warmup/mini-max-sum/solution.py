#!/bin/python3

def minSum(arr):
    arr.remove(max(arr))
    return sum(arr)

def maxSum(arr):
    arr.remove(min(arr))
    return sum(arr)

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(minSum(arr.copy()), maxSum(arr.copy()))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
