#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if (n%2!=0) or (n%2==0 and n in range(6,20+1)):
    print("Weird")
if (n%2==0 and n in range(2,5)) or (n%2==0 and n>20):
    print("Not Weird")

