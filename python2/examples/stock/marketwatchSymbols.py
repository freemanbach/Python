#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.15
# Version : 0.0.1
# Desc    : Financial Stock Program
#         : Pull MarketWatch Symbols
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
    parta = "https://www.marketwatch.com/tools/mutual-fund/list/"
    print "Building links..."
    for i in string.ascii_uppercase:
        symbolsLink.append(parta+i)

    return symbolsLink


def parseData(rlinks):
    random.seed(time.time)
    data, data2, symbols = [], [], []
    for lk in rlinks:
        t = random.randint(1,3)
        page = requests.get(lk)
        goop = BeautifulSoup(page.text, 'html.parser')
        time.sleep(1+t)
        print "Building Mutual Fund: " + str(lk) + " ticker info."
        aTags = goop.find_all('a', href=True)
        for a in aTags:
            if "Class C" in str(a):
                data.append(str(a))

        for i in data:
            if "href" in str(i):
                data2.append(str(i))

        for i in data2:
            a = i.split("\"")
            symbols.append(str(a[1].split("/")[3]).strip())
        print "Building Mutual Fund: " + str(lk) + " ticker info: Done."

    # cleaning off some redundant data from marketwatch.com
    # why there were over 500k redundant symbols is beyond me
    symbols.sort()
    symbols = list(dict.fromkeys(symbols))
    symbols.sort()

    return symbols


def writeToFile(bigdata):
    dfile = "MutualFundCLassCTickers.txt"
    fo = open(dfile , "w")
    for i in bigdata:
        fo.write(i+"\n")
    fo.close()


def main():
    val = int(testConn())
    if val == 1:
        print "Internet Connection is ok."
        l = buildLinks()
        print "Building Links: Done"
        x = parseData(l)
        writeToFile(x)
        print
        print "Completed, there should be a file called MutualFundClassCTickers.txt " 
    else:
        print "Your local Internet Connection is down or something wrong with router."
        print "Reboot Router, Switch, Hub or PC or All four ."


if __name__ == "__main__":
    main()
