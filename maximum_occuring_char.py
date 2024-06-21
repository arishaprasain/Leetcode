#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

def maximumOccurringCharacter(text):
    # Write your code here
    hmap = {}
    for char in text:
        if char not in hmap.keys():
            hmap[char] = 0
        else:
            hmap[char] += 1
    
    val = max(hmap.values())
    
    many = []
    for char in hmap.keys():
        if hmap[char] == val:
            many.append(char)
            
    return many[0]    
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = maximumOccurringCharacter(text)

    fptr.write(str(result) + '\n')

    fptr.close()
