#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.09
# Version : 0.0.1
# Desc    : Financial Stock Program
#         : Pull Barron Mutual Fund tickers to a file
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


# Cant seem to locate a list of Mutual Funds as a csv file anywhere.
# besides Barrons, marketwatch was the only other place has this info.
# https://www.marketwatch.com/tools/mutual-fund/list/A
def buildLinks():
    symbolsLink = []
    # humm.... barron data had moved to wall street journal apparently
    parta = "http://interactive5.wsj.com/mdc/public/page/9_3048-usmfunds_" 
    partb = "-usmfunds.html?mod=mdc_h_mfhl"
    #http://interactive5.wsj.com/mdc/public/page/9_3048-usmfunds_B-usmfunds.html?mod=mdc_h_mfhl
    #parta = "http://www.barrons.com/mdc/public/page/9_3048-usmfunds_"
    #partb = "-usmfunds.html"
    print "Building links..."
    for i in string.ascii_uppercase:
        symbolsLink.append(parta+i+partb)

    return symbolsLink


# lack therfore ninja skillz in BS4
# definitely can do better with advance BS4 skillz, this is a hack
# idk why it is slow in wsj.com when compared to barron.com
# there might be a blocking tool in wsj to prevent this crawler from crawling its dataset
def parseData(rlinks):
    random.seed(time.time)
    data, symbols = [], []
    for lk in rlinks:
        t = random.randint(1,3)
        page = requests.get(lk)
        goop = BeautifulSoup(page.text, 'html.parser')
        time.sleep(1+t)
        print "Building Mutual Fund: " + str(lk) + " ticker info."
        for a in goop.find_all('a', href=True):
            if len(a.text) == 5:
                symbols.append(str(a.text).strip())
        print "Building Mutual Fund: " + str(lk) + " ticker info: Done."


    # Great thing that all mutual funds have 'x' as the last character
    for d in symbols:
        if d[len(d)-1].lower() == 'x':
            data.append(d)
    data.sort()
    return data 


def writeToFile(data):
    fo = open("mutualfundtickers.txt", "w")
    for i in data:
        fo.write(i+"\n")
    fo.close()


def main():
    val = int(testConn())
    if val == 1:
        print "Internet Connection is ok."
        l = buildLinks()
        print "Building Links: Done"
        a = parseData(l)
        writeToFile(a)
        print
        print "Completed, there should be a file called mutualfundtickers.txt"
    else:
        print "Your local Internet Connection is down or something wrong with router."
        print "Reboot Router, Switch, Hub or PC or All four ."


if __name__ == "__main__":
    main()
