import math
import os
import random
import re
import sys

def timeConversion(s):
    if s[-2:]=='AM' and s[:2]=='12':
        s=s.replace(s[:2],'00',1)
    elif s[-2:]=='PM' and s[:2]!='12':
        s=s.replace(s[:2],str(int(s[:2])+12),1)
        
    return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
