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
    except ImportError:
        print "Missing Plugin, download BeautifulSoup version 4 "

def chkFileExist():
    try:
        f = open("hobbit.txt", "r")
    except IOError:
        print "File missing, check location "


def chkDivideZero(a,b):
    try:
        print a / b 
    except ZeroDivisionError:
        print "can not divide by zero "


def chkNameError():
    try:
        print 3 * 4 + cheese
    except NameError:
        print "Variable was never assigned a value and variable cannot do the task at hand "

		
def chkTypeError():
    try:
        print "there are " + 8 + " Hobbits on middle earth"
    except TypeError:
        print "Cannot have string to print out with numeric types "

def main():
    chkBeautifulSoup()
    chkFileExist()
    a = input("Enter a value? ")
    b = input("Enter another value? ")
    chkDivideZero(a,b)
    chkNameError()
    chkTypeError()

if __name__ == "__main__":
    main()
