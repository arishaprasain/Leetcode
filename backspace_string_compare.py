#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compareStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def compareStrings(s1, s2):
    # Write your code here
    # l1 = len(s1)
    # l2 = len(s2)
    
    # if l1 != l2:
    #     return 0
    
    if not s1 and not s2:
        return 1
        
    #stacks
    stack1 = []
    stack2 = []
     

    for char in s1:
        if char != '#':
            stack1.append(char)
        elif char == '#':
            try:
                stack1.pop()
            except IndexError:
                continue
                
    
    for char in s2:
        if char != '#':
            stack2.append(char)
        elif char == '#' and stack2:
            stack2.pop()
    
    if not stack2 and not stack1:
        return 1
    
    else:    
        out1 = ''.join(stack1)   
        print(out1)
        
        out2 = ''.join(stack2)     
        print(out2)        
                
        if out1 == out2:
            return 1
            
            
        else:
            return 0        
    
    
            
            
            
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = compareStrings(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
