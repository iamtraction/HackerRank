#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input())

    gmail_users = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.match(r"[a-z.]+@gmail\.com", emailID):
            gmail_users.append(firstName)

    gmail_users.sort()

    for user in gmail_users:
        print(user)
