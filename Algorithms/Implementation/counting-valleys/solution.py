#!/bin/python3

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    start_step = None
    sealevel = uphills = downhills = 0

    for step in s:
        if not start_step:
            start_step = step

        if step == "U":
            sealevel += 1
        elif step == "D":
            sealevel -= 1
        
        if sealevel == 0:
            if start_step == "U":
                uphills += 1
            elif start_step == "D":
                downhills += 1

            start_step = None

    return downhills
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
