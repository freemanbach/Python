# Author  : freeman
# Date    : 2019.05.25
# Version : 0.0.1
# Desc    : Program 1
#         : testing some simple json code
###################################################################


import json
import sys
import requests


def readJson1():
    with open('cakes.json', 'r') as fi:
        ds = json.load(fi)
    return ds


def readJson2():
    mess = ""
    with open('office_data.json', 'r') as fi:
        for i in fi:
            mess += i
    ds = json.loads(mess)
    return ds


def readJson3():
    url = "https://jsonplaceholder.typicode.com/albums"
    data = requests.get(url)
    ds = json.loads(data.text)
    return ds


"""
0: Date; 1: Open; 2: High; 3: Low; 4: Close; 5: Volume
"""
def readJson4():
    with open('fb.json', 'r') as fi:
        ds = json.load(fi)
    d3 = ds['dataset']['data']
    return d3


def main():
    print "Set A:"
    a = readJson1()
    print a
    print "Set B:"
    b = readJson2()
    print b
    print "Set C:"
    c = readJson3()
    print c
    print "Set D:"
    d = readJson4()
    print d

if __name__ == "__main__":
    main()
