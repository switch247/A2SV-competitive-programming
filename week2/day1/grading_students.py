#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    x= len(grades)
    for n in range(x):
        if grades[n] >= 38:
            if grades[n] % 5 == 3:
                grades[n] += 2
            elif grades[n] % 5 == 4:
                grades[n] += 1
        else:
            grades[n]=grades[n]
                
    return grades;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
