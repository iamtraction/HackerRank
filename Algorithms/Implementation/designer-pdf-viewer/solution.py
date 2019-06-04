#!/bin/python3

import os

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    char_heights = [h[ord(c) - 97] for c in word]
    return max(char_heights) * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
