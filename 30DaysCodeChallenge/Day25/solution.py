import math

def primality(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n & 1 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    cases = int(input())

    for case in range(cases):
        print("Prime") if primality(int(input())) else print("Not prime")
