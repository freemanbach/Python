#!/usr/bin/env python3

# Author  : freeman
# Date    : 2019.04.26
# Version : 0.0.1
# Desc    : Program 2
#
###################################################################

import os
import sys
import time


def main():
    a = input("Enter in a string? ")
    print("Hello Planet! " ,  a)
    print("Hello Planet! " +  a)
    b = int(input("Enter in an integer ? "))
    print("Your answer is: " + str(b))
    print("Your answer is: ",  b)

    # Math
    c = 8/5
    print("Answer ist: " , c ) # this is now a decimal in Py3
    d = -8/5
    print("Answer ist: " , d ) # this is now a decimal in Py3

    # String
    print(type("Hello world."))
    print(type(b"Hello world.")) # there is a byte type
    print(type(u"Hello world.")) # unicode and str are the same

    # Range function
    for i in range(1,10): # range() and xrange() in py2 == range() in py3
        print("YOur values are: " + str(i))

    e = range(0,10)
    print(type(e))

    # no longer lists return type
    f = map(float, e)
    print(type(f))
    print(list(f))

    # rounding is horrible with python3
    # cant figureout why it does what it did

    # function zip()
    g = [1,2,3,4,5]
    h = ['a','b','c','d','e']
    i = zip(g,h)
    print(list(i))


def test1():
    try:
        f = open('file.txt', 'r')
        line = f.readline()
        if line == "":
            raise IOError("File not there?")  # it needs the parens
    except IOError as e: # py3 required the as keyword
        print(e , "File is not there ?!")
    else:
        print("no error: ", line)



if __name__ == "__main__":
    main()

