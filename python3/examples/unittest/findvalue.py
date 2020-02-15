#!/usr/bin/env python3


def findLarge(a,b,c):
    max = 0
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    elif b > a:
        if b > c:
            max = b
        else:
            max = c
    return max


def findSmall(a,b,c):
    return 0