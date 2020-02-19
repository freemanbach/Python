#!/usr/bin/env python3

import sys


# if a is {int||float}  -> solution 
# if b is {int||float}  -> solution 
# if a || b is {String} -> NoneType
def add(a,b):
    """
    Exception: except NameError outside of this function
    """
    ans = 0
    if str(type(a)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(a)).split(' ')[1].split('\'')[1].lower() == 'float' and str(type(b)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(b)).split(' ')[1].split('\'')[1].lower() == 'float':
        ans = a+b
        return ans
    return None

# if a is {int||float}  -> solution 
# if b is {int||float}  -> solution 
# if a || b is {String} -> NoneType
def sub(a,b):
    """
    Exception: except NameError outside of this function
    """
    if str(type(a)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(a)).split(' ')[1].split('\'')[1].lower() == 'float' and str(type(b)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(b)).split(' ')[1].split('\'')[1].lower() == 'float':
        return a+b
    return None


# if a is {int||float}  -> solution 
# if b is {int||float}  -> solution 
# if a || b is {String} -> NoneType
def mul(a,b):
    """
    Exception: except NameError outside of this function
    """
    if str(type(a)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(a)).split(' ')[1].split('\'')[1].lower() == 'float' and str(type(b)).split(' ')[1].split('\'')[1].lower() == 'int' or str(type(b)).split(' ')[1].split('\'')[1].lower() == 'float':
        return a+b
    return None


# if divisor is 0 -> 'division by zero'
# if divisor is not 0 -> floatValue
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
