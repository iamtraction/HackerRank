#!/bin/python3

import os

def similarity(s, t):
    simimilar_chars = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            simimilar_chars += 1
        else:
            break
    return simimilar_chars

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    size = len(s) + len(t)

    if size <= k:
        return "Yes"

    min_ops = size - similarity(s, t) * 2
    return "Yes" if k >= min_ops and (k - min_ops) % 2 == 0 else "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
