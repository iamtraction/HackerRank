#!/bin/python3

import os

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c = sorted(c)

    # distance b/w 1st city and 1st space station city
    max_dist = c[0] - 0

    # max distance of cities, b/w the 1st and last
    # space station city, to the nearest space station city
    if len(c) > 1:
        dist = max((c[i + 1] -  c[i]) // 2 for i in range(len(c) - 1))
        if dist > max_dist:
            max_dist = dist

    # distance b/w last space station city and last city
    dist = n - 1 - c[-1]
    if dist > max_dist:
        max_dist = dist

    return max_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
