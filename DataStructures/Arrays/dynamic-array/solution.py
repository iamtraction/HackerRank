#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seq_list = [list() for _ in range(n)]
    last_answers = [0]

    for query in queries:
        if query[0] == 1:
            seq_list[(query[1] ^ last_answers[-1]) % n].append(query[2])
        elif query[0] == 2:
            seq = seq_list[(query[1] ^ last_answers[-1]) % n]
            last_answers.append(seq[query[2] % len(seq)])

    return last_answers[1:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
