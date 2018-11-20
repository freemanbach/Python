#!/usr/bin/env python
# Author  : freeman
# Date    : 2018.11.19
# Version : 0.0.1
# Desc    : Program 5
#         : Functions
###################################################################

import os
import sys
import time
import math

def addTwoNums1():

    a = input("Enter a value? ")
    b = input("Enter a value? ")
    result = a + b
    return result

def addTwoNums2(a,b):

    return float(a + b)

def powwow(base,exp):

    return math.pow(base,exp)

def splitStringiBySpace(a):
    
    return a.split(' ') 

def splitStringByComma(a):

    return a.split(',')

def specialFunc():

    num_list = [1,2,3] 
    ans = [(lambda x : x*2)(x) for x in num_list]
    return ans

def main():

    a = specialFunc()
    print a

if __name__ == "__main__":
    main()
