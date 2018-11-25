# Author  : freeman
# Date    : 2018.11.25
# Version : 0.0.1
# Desc    : Program 8
#
###################################################################

import os
import sys
import time


def chkBeautifulSoup():
    try:
        from bs4 import BeautifulSoup
    except ImportError as err:
        print "Missing Plugin, download BeautifulSoup version 4 "
        exit(1)


def chkFileExist():
    try:
        f = open("hobbit.txt", "r")
    except FileNotFoundError, IOError as err:
        print "File missing, check location " + err
        exit(1)


def chkDivideZero():
    try:
        print 1 / 0 
    except ZeroDivisionError as err:
        print "cantnot divide by zero " + err
        exit(1)


def chkNameError():
    try:
        print 3 * 4 + cheese
    except NameError as err:
        print "Variable was never assigned a value and variable cannot do the task at hand " + err
        exit(1)


def chkTypeError():
    try:
        print "there are " + 8 + " Hobbits on middle earth"
    except TypeError as err:
        print "Cannot have string to print out with numeric types " + err
        exit(1)


def main():


if __name__ == "__main__":
    main()
