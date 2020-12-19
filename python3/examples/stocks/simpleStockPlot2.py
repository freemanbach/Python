#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.06.09
# Version : 0.0.1
# Desc    : A Program which will build a plot chart for you 
#         : when you supply it with a stock symbol or a mutual fund 
#         :  symbol: saves to a png img file
###################################################################


import time
import random as rnd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from datetime import datetime
from calendar import monthrange
from datetime import timedelta


def getTicker():
    # one of these might not be a stock ticker
    tickers = ['fb', 'goog', 'aapl', 'ibm', 'csco', 'mrk', 'lly', 'pfe', 'sny', 'bsx', 'xom', 'bp', 'db']
    ticks = list()
    rnd.seed(time.time())
    items = len(tickers) % 5
    for i in range(items):
        ticks.append(tickers[rnd.randint(0, len(tickers)-1)])

    return ticks


def getDates():
    ctl, otl = [], []
    ct = datetime.now()
    cy = ct.year
    cm = ct.month - 1
    cdays = monthrange(cy, cm)[1]
    ctl.append(cy)
    ctl.append(cm)
    ctl.append(cdays)
    ot = ct - timedelta(days=180)
    oy = ot.year
    om = ot.month
    odays = monthrange(oy, om)[1]
    otl.append(oy)
    otl.append(om)
    otl.append(odays)

    return ctl, otl


# year, month, day
def getStockChart(cdates, pdates, tags):

    for i in range(len(tags)):
        tmp = str(tags[i])
        fname = str(tmp)
        ticker = pdr.get_data_yahoo(symbols=tmp, start=datetime(int(pdates[0]),int(pdates[1]),int("1")), end=datetime(int(cdates[0]),int(cdates[1]),int(cdates[2])) )
        ticker.Close.plot(label=tmp)
        plt.xlabel("date")
        plt.ylabel("price")
        plt.title(tmp)
        plt.legend(loc='upper left')
        # you can uncomment this to save each chart as a png file
        #plt.savefig(fname, bbox_inches='tight')
        plt.show()
        plt.clf()


def main():
    a1, b1 = getDates()
    c1 = getTicker()
    getStockChart(a1, b1, c1)


if __name__ == "__main__":
    main()
