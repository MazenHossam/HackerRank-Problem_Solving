import math
import os
import random
import re
import sys


def getTotalX(a, b):
    count=0
    for i in range(a[0],b[0]+1):
        if (sum(i%x==0 for x in a)) + (sum(x%i==0 for x in b)) == len(a)+len(b):
            count+=1
    return count

  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
