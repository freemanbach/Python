"""
author     : freeman
date       : 20201012
desc       : Pull covid data from covidtracking.com over json api
           : it will generate a csv file after it ran.
exec       : python3 getCOVdata.py US_state
example    : python3 getCOVdata.py nc
"""


from requests.exceptions import HTTPError
from datetime import datetime
import requests
import json
import sys


def fixdate(d):
    # sublimate Date
    dateitem = datetime(year=int(d[0:4]), month=int(d[4:6]), day=int(d[6:8]))
    dt = str(dateitem.year)+"-"+str(dateitem.month)+"-"+str(dateitem.day)
    return dt


def pullJSON(sa):
    # Having flexible US State Abbreviation to generate csv file
    state = "https://api.covidtracking.com/v1/states/" + sa + "/daily.json"
    try:
        resp = requests.get(state)
        resp.raise_for_status()
        jsondata = resp.text
    except HTTPError as herr:
        print("Http Connection Error", herr)
        sys.exit()

    return jsondata


def processJSON(jsdata):
    # more data Attributes to consider in the future, perhaps
    # date, positive, hospitalizedCumulative, death, deathConfirmed, positiveIncrease, total
    # vapos, vahospcum, vaposinc, vahospinc = [], [], [], [], [], [], []
    vadate,  vadeath, vadeathconfirm = [], [], [] 
    data = json.loads(jsdata)
    for i in data:
        if len(str(i['date'])) == 8:
            vadate.append(fixdate(str(i['date'])))
        if str(i['death']).isdigit():
            vadeath.append(int(i['death']))
        else:
            vadeath.append(0)
        if str(i['deathConfirmed']).isdigit():
            vadeathconfirm.append(int(i['deathConfirmed']))
        else:
            vadeathconfirm.append(0)
    # reverse data points
    vadeathconfirm.reverse()
    vadate.reverse()
    vadeath.reverse()

    return vadate, vadeath, vadeathconfirm
    

def writeData( a, b, c, nf ):
    # heading for csv file to prep for plotly.JS
    # Date,VADATA.Death,VADATA.DeathConfirmed
    data = []
    fn = nf.strip() + "data.csv" 
    for i in list(range(0, len(a))):
        m = str(a[i]).strip() + "," + str(b[i]).strip() + "," + str(c[i]).strip() + "\n"
        data.append(m)

    head = "Date,"+ nf.upper() + "DATA.Death," +  nf.upper() + "DATA.DeathConfirmed\n"
    
    data.insert(0, head)
    with open(fn, "w+") as f:
        for i in data:
            f.write(i)
    

def main():
    # VOODOO Magik
    if len(sys.argv) == 2:
        xz = sys.argv
        a = pullJSON(str(xz[1]).strip())
        x,y,z = processJSON(a)
        writeData( x, y, z, str(xz[1]))
    else:
        print("not enough parameters.")
        sys.exit()


if __name__ == "__main__":
    main()