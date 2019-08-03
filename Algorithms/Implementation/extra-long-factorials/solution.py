#!/bin/python3

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
