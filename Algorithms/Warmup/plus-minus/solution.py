#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    print(sum(1 if i > 0 else 0 for i in arr) / len(arr))
    print(sum(1 if i < 0 else 0 for i in arr) / len(arr))
    print(sum(1 if i == 0 else 0 for i in arr) / len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
