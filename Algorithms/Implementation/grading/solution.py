#!/bin/python3

import os

# Complete the gradingStudents function below.
def gradingStudents(grades):
    # Write your code here.
    return (i + 5 - i % 5 if i > 37 and i % 5 > 2 else i for i in grades)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
