import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    day='13'
    if (year<1918 and year%4==0) or (year>1918 and (year%400==0 or (year%4==0 and not year%100==0))):
        day='12'            
    elif year==1918:
        day='26'        
    return("{}.{}.{}".format(day,'09',year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
