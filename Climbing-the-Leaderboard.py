#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    #del dups
    newScores = list(dict.fromkeys(scores))
    answer = []

    for i in alice:
        start = 0
        end = len(newScores) - 1
        cstart = start
        cend = end

        while ( start <= end ):
            middle = (start + end) // 2
            if newScores[middle] == i:
                answer.append(middle)
                break
            elif newScores[middle] > i:
                if middle == cend:
                    answer.append(cend+1)
                    break
                if (newScores[middle+1] < i):
                    answer.append(middle + 1)
                    break
                start = middle + 1
            else:
                if middle == cstart:
                    answer.append(cstart)
                    break
                if (newScores[middle-1]) > i:
                    answer.append(middle)
                    break
                end = middle -1

    return ([x + 1 for x in answer ])


a = [100, 90, 90, 80, 75, 60]
b = [50, 65, 77, 90, 102]

print(climbingLeaderboard(a , b))





