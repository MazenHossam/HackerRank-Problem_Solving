#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    # count=0
    
    # for i in range(len(ar)):
    #     count+= sum((ar[i]+j)%k==0 for j in ar[i+1:])
    
    # return count
    return sum((ar[i]+j)%k==0 for i in range(len(ar)) for j in ar[i+1:] )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
