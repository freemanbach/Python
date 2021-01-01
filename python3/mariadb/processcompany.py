#!/bin/env python3

"""
author     : freeman
date       : 20200101
desc       : Process Nasdaq Stock Data into sql for company table
           : 
use        : python3 processcompany.py ns.csv companyData.sql
           :
"""

import sys
import random

def processdata(item, output):
    data = []

    with open(item, 'r') as f:
        for i in f:
            line = i.split(',')
            z = line[0].strip().lower()
            z = z.replace("/", "")
            
            y = line[9].strip().lower()
            y = y.replace("&", " and ")
            y = y.replace("(", "")
            y = y.replace(")", "")
            y = y.replace("/", " ")
            y = y.replace("'", " ")
            
            x = line[10].strip().lower()
            x = x.replace("&", " and ")
            x = x.replace("(", "")
            x = x.replace(")", "")
            x = x.replace("/", " ")
            x = x.replace("'", " ")

            w = line[1].strip().lower()
            w = w.replace("'", " ")
            w = w.replace("(", "")
            w = w.replace(")", "")
            w = w.replace("&", " and ")
            w = w.replace("'", " ")
            w = w.replace(".", " ")

            a = "INSERT INTO company (name, ticker, description, sector, industry) VALUES (" + "\'" + z + "\'" +  ","   \
                + "\'" + z + "\'" + "," \
                + "\'" + w + "\'" + "," \
                + "\'" + y + "\'" + "," \
                + "\'" + x + "\'" + ");" + "\n" 
            data.append(a)
    data.pop(0)
    data.insert(0, "use simplefinance;\n")

    with open( output, "w") as f:
        for i in data:
            f.write(i)

def getsymbols():
    symbols, tmp = [], []
    with open( "ns.csv", "r") as f:
        for i in f:
            a = str(i.split(",")[0]).strip().lower()
            a = a.replace(".", "")
            a = a.replace("/", "")
            tmp.append(str(a)+"\n")
    for i in list(range(0,10)):
        symbols.append(random.choice(tmp))

    print(symbols)
    with open("symbols.txt", "w") as f:
        for i in symbols:
            f.write(str(i))


def main():
    if len(sys.argv) == 3:
        dfile = sys.argv[1]
        ofile = sys.argv[2]
        processdata(str(dfile), str(ofile))
        getsymbols()
    else:
        print("Not enough parameters.")
        print("See Header Information.")

if __name__ == "__main__":
    main()