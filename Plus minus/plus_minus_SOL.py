import math
import os
import random
import re
import sys

# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    sums=[0,0,0]
    for i in arr:
        if i>0: sums[0]+=1;
        elif i<0: sums[1]+=1;
        else: sums[2]+=1;
    print ("{}\n{}\n{}\n".format(sums[0]/len(arr),sums[1]/len(arr),sums[2]/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
