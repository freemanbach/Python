#!/usr/bin/env python3

import sys


def add(a,b):
    return a+b


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


# if divisor == 0 -> None
# if divisor != 0 -> floatValue
def div(a,b):
    z = 0
    try:
        z = a / b
    except ZeroDivisionError as oh:
        print(oh)
    else:
        return z


def procname( name ):
    flname = name.split(' ')
    fname = flname[0][0] + '.' + flname[1]
    return fname
    
    
def procamount( cost ):
    return float(cost) * 1.20


def chkgrade(num):
    
    if float(num) >= 90:
        return 'A'
    elif float(num) >= 80:
        return 'B'
    elif float(num) >= 70:
        return 'C'
    elif float(num) >= 60:
        return 'D'
    else:
        return 'F'