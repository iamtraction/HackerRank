#!/bin/python3

def is_kaprekar_number(n):
    digits = len(str(n))
    square = str(n * n)

    if int(square[:-digits] or 0) + int(square[-digits:] or "0") != n:
        return False

    return True

# Complete the kaprekarNumbers function below.
def kaprekar_numbers(p, q):
    return [str(i) for i in range(p, q + 1) if is_kaprekar_number(i)]

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    result = kaprekar_numbers(p, q)

    if len(result):
        print(" ".join(result))
    else:
        print("INVALID RANGE")
