#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.06.04
# Version : 0.0.1
# Desc    : 
#         : 
#         : 
###################################################################


import warnings
import sys
import requests


def pullData():
    mess, fdata = "", []
    urlData = "https://archive.ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data"
    data = requests.get(urlData)
    a = (data.text).split("\n")

    for i in a:
        tmp = i.split()
        for b in range(len(tmp)):
            mess += tmp[b] + ','
        mess = mess[:-1]
        mess += "\n"
        fdata.append(mess)
    return fdata


def main():
    hob = pullData()
    for i in hob:
        print i


if __name__ == "__main__":
    main()
