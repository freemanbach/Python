#!/usr/bin/env python
# Author  : freeman
# Date    : 2019.05.09
# Version : 0.0.1
# Desc    : Financial mutual fund Program
#         : Pull NASDAQ Trader Mutual funds ticker tags to a file
#         : 
###################################################################


import warnings
import sys
import socket

try:
    import ftplib
except ImportError as err:
    warnings.warn('No Package named urllib3 was found. ', ImportWarning)
    print(err.__class__.__name__ + ": " + err.message)
    sys.exit(1)


def testConn():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as err:
        print("No Connection: " + err.errno)
    return False


def retrieveFile():
    url = 'ftp://ftp.nasdaqtrader.com/symboldirectory/mfundslist.txt'
    return stuff


def processData(rData):

    mfsymbols = []
    print("Pocessing Mutual Funds Symbols.")
    for z in range(1, len(rData)-1):
        mfsymbols.append(rData[z].split('|')[0].strip()) 
    print("Processing Mutual Funds Symbols: Done.")

    return mfsymbols


def writeToFile(data):
    fo = open("mutualFunds.txt", "w")
    for i in data:
        fo.write(i+"\n")
    fo.close()


def main():
    val = int(testConn())
    if val == 1:
        print("Internet Connection is ok.")
        dt = retrieveFile()
        s = processData(dt)
        writeToFile(s)
        print("\n")
        print("Completed, there should be a file called mutualFunds.txt")
    else:
        print("Your local Internet Connection is down or something wrong with router.")
        print("Reboot Router, Switch, Hub or PC or All four .")


if __name__ == "__main__":
    main()
