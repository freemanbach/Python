# Author  : freeman
# Date    : 2020.03.30
# Version : 0.0.1
# Desc    : Program 1
#         : Parsing json data from alphaadvantage.co
#         : Parsing these json files seems to be a bit tricky
###################################################################


import json
import sys

"""
Dictionary inside another dictionary
{Date; {1: Open: value; 2: High: value; 3: Low: value; 4: Close: value; 5: Volume: value}}
"""
def processItems(fdsa):

    openditem, highditem, lowditem, closeditem, volditem = {}, {}, {}, {}, {}

    for k, v in fdsa.items():
        #dateitem.append(str(k).strip())
        x = str(k).strip()
        for a, b in v.items():
            if str(a).strip() == "4. close":
                closeditem[x] = str(b).strip()
            if str(a).strip() == "1. open":
                openditem[x] = str(b).strip()
            if str(a).strip() == "2. high":
               highditem[x] = str(b).strip()
            if str(a).strip() == "3. low":
                lowditem[x] = str(b).strip()
            if str(a).strip() == "5. volume":
                volditem[x] = str(b).strip()

    for o, p in openditem.items():
        print(o ,  "  " , p)


def readJson():
    with open('aaplAlpha.json', 'r') as fi:
        ds = json.load(fi)
        tds = ds['TimeSeries']
    return tds


def main():
    tmp = readJson()
    processItems(tmp)


if __name__ == "__main__":
    main()
