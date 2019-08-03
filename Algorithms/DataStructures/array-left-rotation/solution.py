#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    a = [str(i) for i in a[d:] + a[:d]]

    print(' '.join(a))
