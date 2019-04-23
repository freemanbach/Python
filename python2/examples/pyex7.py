# Author  : freeman
# Date    : 2018.11.24
# Version : 0.0.1
# Desc    : Program 7
#
###################################################################

import os
import sys
import time


def main():

    f = open("test.data", "r")
    lst, cnt = [], 0
    for y in f:
        a = y.rstrip('\r\n')
        a = a.split(" ")
        for z in a:
            cnt += len(z)
            if z != "":
                lst.append(z)
            else:
                continue   
    print str(lst)
    print "the numbere of chars ist: " + str(cnt)
    f.close()


if __name__ == "__main__":
    main()
