#!/bin/python3

import os

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    timely_arrivals = list(filter(lambda x: x <= 0, a))
    return "YES" if len(timely_arrivals) < k else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
