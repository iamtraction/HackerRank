#!/bin/python3

import os

# Complete the breakingRecords function below.
def breakingRecords(scores):
    records =  [ scores[0], scores[0] ]
    breaks = [ 0, 0 ]

    for score in scores:
        if score > records[0]:
            records[0] = score
            breaks[0] += 1
        elif score < records[1]:
            records[1] = score
            breaks[1] += 1

    return breaks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
