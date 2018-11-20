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


def splitStringBySpace(a):
    
    return a.split(' ') 


def splitStringByComma(a):

    return a.split(',')


def specialFunc():

    num_list = [1,2,3] 
    ans = [(lambda x : x*2)(x) for x in num_list]
    return ans


def countItems1():

    a = ["mary", "had" , "a", "sheep"]
    print len(a)


def countItems2():

    cnt = 0
    a = ["mary", "had", "a", "giant","sheep"]
    for i in a:
        cnt+=1

    print "the number of items in this list ist: " + str(cnt)


def testOddEven():

    even = []
    odd = []
    for i in range(0,200):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd


def main():

    a = specialFunc()
    print a

    e, o = testOddEven()
    print "Even list: " + str(e)
    print "Odd list: " + str(o)


if __name__ == "__main__":
    main()
