#!/usr/bin/env python3

# Author  : freeman
# Date    : 2019.05.01
# Version : 0.0.1
# Desc    : Program 3
#
###################################################################

import os
import sys
import time


def main():
    ui = input("Enter in a equation with equal symbol at the end: ")
    values = list(ui.strip().split())
    if values[len(values)-1] == '=':
        #print(values)
        if values[1] == '+':
            print(float(values[0]) + float(values[2]))
        elif values[1] == '-':
            print(float(values[0]) - float(values[2]))
        elif values[1] == '*':
            print(float(values[0]) * float(values[2]))
        elif values[1] == '/':
            print(float(values[0]) / float(values[2]))
        else:
            print("i dont know")
    else:
        print("Must have an equal Symbol in the end of your math expression!!")


if __name__ == "__main__":
    main()
