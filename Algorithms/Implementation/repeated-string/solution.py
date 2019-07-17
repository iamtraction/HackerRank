#!/bin/python3

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count("a") * int(n / len(s)) + s[:n % len(s)].count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
