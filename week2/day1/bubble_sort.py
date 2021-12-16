#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    index = len(a)
    count = 0
    for i in range(index):
         for i in range(index-1):
             if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count = count + 1
    first = a[0]
    last = a[-1]

    print("Array is sorted in",count,"swaps.")
    print("First Element:", first)
    print("Last Element:", last)
    
         


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

    

