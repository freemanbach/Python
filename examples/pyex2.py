#!/usr/bin/env python
# Author  : freeman
# Date    : 2018.11.17
# Version : 0.0.1
# Desc    : Program 2
#
###################################################################

import os
import sys
import time


def main():

    # let us prompt the user for something
    ui1 = raw_input("Enter in a string of words? ")
    ui2 = raw_input("Enter in another string of words? ")

    # we are going to add them together
    ui3 = ui1 + " " + ui2

    # printing out concatnated string
    print ui3


if __name__ == "__main__":
    main()
