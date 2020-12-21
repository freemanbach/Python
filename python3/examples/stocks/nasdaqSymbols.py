#!/usr/bin/env python
# Author  : freeman
# Date    : 2020.12.20
# Version : 0.0.1
# Desc    : Financial Stock Program
#         : Pull NASDAQ stock ticker tags to a file
# updated : https://www.nasdaq.com/market-activity/stocks/fb 
#         : New Site:
#         : https://www.advfn.com/nasdaq/nasdaq.asp?companies=A
###################################################################


import warnings
import sys


try:
    import pandas as pd
except ImportError as err:
    warnings.warn('No Package named pandas available', ImportWarning)
    print(err.__class__.__name__ + ": " + err.message)
    sys.exit(1)


import string
import time
import random
import socket


try:
    from bs4 import BeautifulSoup
except ImportError as err:
    warnings.warn('No Package named BeautifulSoup was found. ', ImportWarning)
    print(err.__class__.__name__ + ": " + err.message)
    sys.exit(1)


try:
    import requests
except ImportError as err:
    warnings.warn('No package named Requests was found. ', ImportWarning)
    print(err.__class__.__name__ + ": " + err.message)
    sys.exit(1)


def testConn():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as err:
        print("No Connection: " + err.errno)
    return False


def buildLinks():
    symbolsLink = []
    # http://eoddata.com/stocklist/NASDAQ/A.htm
    parta = "https://www.advfn.com/nasdaq/nasdaq.asp?companies="
    # "https://www.nasdaq.com/screening/companies-by-name.aspx?letter="
    # partb = "&render=download"
    print("Building links...")
    for i in string.ascii_uppercase:
        symbolsLink.append(parta+i)

    return symbolsLink


def parseData(rlinks):
    random.seed(time.time)
    data, symbols = [], []
    for lk in rlinks:
        t = random.randint(1,4)
        page = requests.get(lk)
        goop = BeautifulSoup(page.text, 'html.parser')
        time.sleep(1+t)
        print("Building Mutual Fund: " + str(lk) + " ticker info.")
        for a in goop.find_all('a', href=True):
            # Stocks has len == 4 from this website
            if len(a.text) == 4:
                symbols.append(str(a.text).strip())
        print("Building Mutual Fund: " + str(lk) + " ticker info: Done.")

    # This should all be stock symbols
    for d in symbols:
            data.append(d)
    data.sort()

    return data


def writeToFile(data):
    fo = open("tickers.txt", "w")
    for i in data:
        fo.write(i+"\n")
    fo.close()


def main():
    val = int(testConn())
    if val == 1:
        print("Internet Connection is ok.")
        l = buildLinks()
        print("Building Links: Done")
        a = parseData(l)
        writeToFile(a)
        print("\n")
        print("Completed, there should be a file called tickers.txt")
    else:
        print("Your local Internet Connection is down or something wrong with router.")
        print("Reboot Router, Switch, Hub or PC or All four .")


if __name__ == "__main__":
    main()
