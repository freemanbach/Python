# Author  : freeman
# Date    : 2019.04.09
# Version : 0.0.1
# Desc    : Program 11
#         : python Error handling -- simple Error handling example
###################################################################

import os
import sys

def test1():
    x = int(raw_input("Enter in a number? "))
    y = int(raw_input("Enter in a zero ? "))
    try:
        z = x / y
    except ZeroDivisionError:
        print "Divide by Zero"


def test2():
    try:
        import BeautifulSoup4
    except ImportError:
        print "No lib named as such"


def test3():
    a = [1,2,3]
    try:
        print a[4]
    except IndexError:
        print " no such index is available"


def test4():
    try:
        print "Press return or CTRL-C"
        ignore = raw_input()
    except KeyboardInterrupt:
        print "Caught Keyboard Interrupt"
    else:
        print "no exception"


def test5():
    try:
        a = int(raw_input("Enter in a value? "))
        if a <=0:
            raise ValueError("not a positive value")
    except ValueError as e:
        print e


def test6():
    try:
        a = int(5)
        b = str('a')
        c = a + b
    except TypeError:
        print "caught Type Error exception"
    else:
        print "No exception"


def test7():
    try:
        f = open('file.txt', 'r')
        line = f.readline()
    except IOError as e:
        print "File is not there ?!?!?!?!"
    else:
        print "no error: " + line


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


if __name__ == "__main__":
    main()
