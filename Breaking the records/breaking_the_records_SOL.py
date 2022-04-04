import math
import os
import random
import re
import sys


def breakingRecords(scores):
    max=min=scores[0]
    records=[0,0]
    for i in scores[1:]:
        if i>max:
            max=i
            records[0]+=1
        elif i<min:
            min=i
            records[1]+=1
            
    return records

  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
