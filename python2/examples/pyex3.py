#!/usr/bin/env python
# Author  : freeman
# Date    : 2018.11.17
# Version : 0.0.1
# Desc    : Program 3
#
###################################################################

import os
import sys
import time


def main():

    # let us prompt the user for numeric values
    ui1 = input("Enter in a value? ")
    ui2 = input("Enter in another value? ")

    # we are going to add them together
    ui3 = ui1 + ui2

    # printing out concatnated string
    print "Your answer ist: " + str(ui3)


if __name__ == "__main__":
    main()
