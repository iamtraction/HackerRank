#!/bin/python3

import os
import operator
import bisect

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # We're using the inbuilt bisect library because it's very efficient
    # compared to the 2nd version of this method.
    scores = list(set(scores))
    scores.sort()

    alices_ranks = []

    for score in alice:
        alices_ranks.append(len(scores) - bisect.bisect_right(scores, score) + 1)

    return alices_ranks

def climbingLeaderboard_2(scores, alice):
    # This is very inefficient because of the time complexity of the operations.
    alices_ranks = []

    for score in alice:
        scores.append(score)
        ranks = list(set(scores))
        ranks.sort(reverse=True)
        alices_ranks.append(operator.indexOf(ranks, score) + 1)

    return alices_ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
