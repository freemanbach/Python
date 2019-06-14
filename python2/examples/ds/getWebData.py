#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.06.04
# Version : 0.0.1
# Desc    : Pull dataset from UC Irvine and modify its data
#         : by adding commas between each fields.
#         : 
###################################################################


import warnings
import sys
import requests


def pullData():

    mess, cnt, fdata = "", 0, []
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
        mess=""

    return fdata


def writeToFile(dFile):

    fo = open('ecoli_mod.data', 'w')
    for i in dFile:
        fo.write(i)
    fo.close()


def main():

    hob = pullData()
    writeToFile(hob)


if __name__ == "__main__":
    main()
