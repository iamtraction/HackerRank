#!/bin/python3

import os
from itertools import combinations 

# Complete the acmTeam function below.
def acmTeam(attendees):
    topics = ['{1:0{0}b}'.format(len(team[0]), int(team[0], 2) | int(team[1], 2)).count("1") for team in combinations(attendees, 2)]

    max_topics = max(topics)
    
    return (max_topics, topics.count(max_topics))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
