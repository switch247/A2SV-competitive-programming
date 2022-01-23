#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])% k == 0:
                res+=1
    return( res )
  #what better time to use combinations, i recomend not doing it 
   ''' count = 0
    ar.sort()
    for i in combinations(ar,2):
        if ( sum(i) )%k == 0:
            count+=1
    return count
   
   '''
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
