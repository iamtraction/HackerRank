#!/bin/python3

import os

# Complete the stones function below.
def stones(n, a, b):
    # assuming a < b
    # min possible value is a * (n - 1) or a * (n - 1 - 0) + b * 0 
    # max possible value is b * (n - 1) or a * (n - 1 - n - 1) + b * (n - 1)
    # generalizing the formula and iterating for n, we'll get our answer
    return sorted({ a * (n - 1 - i) + b * i for i in range(n) })

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
