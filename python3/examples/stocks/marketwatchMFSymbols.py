#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.29
# Version : 0.0.1
# Desc    : Financial Stock Program
#         : Pull marketwatch ALL Mutual Fund tags to a file
#         : 
###################################################################


import warnings
import sys


try:
    from bs4 import BeautifulSoup
except ImportError as err:
    warnings.warn('No Package named BeautifulSoup was found. ', ImportWarning)
    print err.__class__.__name__ + ": " + err.message
    sys.exit(1)


try:
    import requests
except ImportError as err:
    warnings.warn('No package named Requests was found. ', ImportWarning)
    print err.__class__.__name__ + ": " + err.message
    sys.exit(1)


import string
import time
import random
import urllib2
import socket


def testConn():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as err:
        print "No Connection: " + err.errno
    return False


def buildLinks():
    symbolsLink = []
    parta = "https://www.marketwatch.com/tools/mutual-fund/list?firstLetter="
    print "Building links..."
    for i in string.ascii_uppercase:
        symbolsLink.append(parta+i)

    return symbolsLink


def buildTicker(sLink):
    stockSymbol, symbols = [], []
    random.seed(time.time)

    for z in sLink:
        t = random.randint(1,3)
        page = requests.get(z)
        goop = BeautifulSoup(page.text, 'html.parser')
        time.sleep(1+t)

        print "Building Mutual Fund: " + str(z) + " ticker info."
        for lk in goop.findAll('td', attrs={'class':'quotelist-symb'}):
            stockSymbol.append(str(lk.find('a').contents[0]).strip())

        for i in stockSymbol:
            symbols.append(i)
        print "Building Stock " + z + " ticker info: done."

    symbols.sort()
    symbols = list(dict.fromkeys(symbols))
    symbols.sort()

    return symbols


def writeToFile(data):
    fo = open("marketWatchMFTickers.txt", "w")
    for i in data:
        fo.write(i+"\n")
    fo.close()


def main():
    val = int(testConn())
    if val == 1:
        print "Internet Connection is ok."
        l = buildLinks()
        print "Building Links: Done"
        a = buildTicker(l)
        writeToFile(a)
        print
        print "Completed, there should be a file called marketWatchMFTickers.txt"
    else:
        print "Your local Internet Connection is down or something wrong with router."
        print "Reboot Router, Switch, Hub or PC or All four ."


if __name__ == "__main__":
    main()
