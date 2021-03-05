# author
# date
# desc
# assign
# version 0.0.1
################################################

"""
Option 1
I will rework my existing python script to pull *COV2 data* from an international Data Bank Our World in Data to retrieve two fields, 
Date and One Country as a CSV file then use either ChartJS or ChartistJS to plot those values. 
You must be able to have a github account and deposit those COV2 data into your public Github account. I will provide a variety of countries for you to choose from a 
list of countries (Australia, New Zealand, Germany, Spain,  France, Poland, Italy, Portugal, Hungary, Austria, and maybe russia). 
    
Option 2)
I will rework my existing python script to pull  *Financial data* from a respected Financial Data Bank to retrieve two fields, Date and a Stock Ticker (Company)  
on using either the Open/Close daily price.  You must then use either ChartJS or ChartistJS to plot those values into a graph.  You must be able to have a github account and 
deposit those Financial data into your public Github account. I will provide a variety of stock ticker (open || close) price as a CSV file for you to choose from a list of companies 
(FB, Google, Amazon, Apple, Netflix, IBM, Uber, J&J, Moderna, Pfizer, and  Oracle, Biontech ). 

https://covid.ourworldindata.org/data/owid-covid-data.csv
AUS,Oceania,Australia
FRA,Europe,France
DEU,Europe,Germany
ESP,Europe,Spain
NZL,Oceania,New Zealand
ITA,Europe,Italy
POL,Europe,Poland,2021-02-20
PRT,Europe,Portugal
HUN,Europe,Hungary
AUT,Europe,Austria
        
country 2, date 3, cases 4, death 7, hospitalization 19, testing 26, vaccination 34
(iso_code,continent,location,date),(total_cases)(total_deaths)(hosp_patients)(total_tests),(total_vaccinations)
"""


try:
    from tqdm import trange, tqdm
except ImportError as herr:
    print("Missing tqdm lib.")


try:
    from requests.exceptions import HTTPError
    import requests
except ImportError as herr:
    print("Missing requests library")


from datetime import datetime
import csv
import sys


def fixdate(d):
    # sublimate Date
    dateitem = datetime(year=int(d[0:4]), month=int(d[4:6]), day=int(d[6:8]))
    dt = str(dateitem.year)+"-"+str(dateitem.month)+"-"+str(dateitem.day)
    return dt


def pullCSV():
    # download the data from ourworldindata.org
    site = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    try:
        resp = requests.get(site)
        resp.raise_for_status()
        csvdata = resp.text
        with open('owid-covid-data.csv', 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            for i in resp.iter_lines():
                w.writerow(i.decode('utf-8').split(','))
    except HTTPError as herr:
        print("Http Connection Error", herr)
        sys.exit()


def procAut():
    # https://www.geeksforgeeks.org/python-reverse-dictionary-keys-order/
    #  country 2, date 3, cases 4, death 7, hospitalization 19, testing 26, vaccination 34
    # country 2, date 3, cases 4, death 7, hospitalization 19, testing 26, vaccination 34
    # (iso_code,continent,location,date),(total_cases)(total_deaths)(hosp_patients)(total_tests),(total_vaccinations)
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Australia":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
                
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv


def procAst():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Austria":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )

    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procFra():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "France":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
                
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procDeu():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Germany":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
                
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procHun():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Hungary":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
            
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procIta():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Italy":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
                
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procNza():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "New Zealand":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )

    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procPol():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Poland":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )

    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procPor():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Portugal":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )

    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def procSpa():
    dcases, ddeath, dhosp, dtest, dvacc = {}, {}, {}, {}, {}
    a = 0
    with open("owid-covid-data.csv", "r") as f:
        for i in f:
            line = i.split(',')
            if line[2] == "Spain":
                if str(line[4]).strip() == None or str(line[4]).strip() == '' or str(line[4]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[4]).strip()))
                dcases.update( {str(line[3]).strip() : a } )
                if str(line[7]).strip() == None or str(line[7]).strip() == '' or str(line[7]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[7]).strip()))
                ddeath.update( {str(line[3]).strip() : a } )
                if str(line[19]).strip() == None or str(line[19]).strip() == '' or str(line[19]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[19]).strip()))
                dhosp.update( {str(line[3]).strip() : a } )
                if str(line[26]).strip() == None or str(line[26]).strip() == '' or str(line[26]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[26]).strip()))
                dtest.update( {str(line[3]).strip() : a } )
                if str(line[34]).strip() == None or str(line[34]).strip() == '' or str(line[34]).strip().isspace():
                    a = 0
                else:
                    a = int(float(str(line[34]).strip()))
                dvacc.update( {str(line[3]).strip() : a } )
                
    res_dc = dict(reversed(list( dcases.items() )))
    res_dd = dict(reversed(list( ddeath.items() )))
    res_dh = dict(reversed(list( dhosp.items() )))
    res_dt = dict(reversed(list( dtest.items() )))
    res_dv = dict(reversed(list( dvacc.items() )))

    return res_dc, res_dd, res_dh, res_dt, res_dv

def writeData( a, b, c, d, e ):
    #  return res_dc, res_dd, res_dh, res_dt, res_dv
    data = []
    fn = nf.strip() + "data.csv" 
    for i in list(range(0, len(a))):
        m = str(a[i]).strip() + "," + str(b[i]).strip() + "," + str(c[i]).strip() + "\n"
        data.append(m)

    head = "Date,"+ nf.upper() + "DATA.Death," +  nf.upper() + "DATA.DeathConfirmed\n"
    
    data.insert(0, head)
    with open(fn, "w+") as f:
        for i in tqdm(data, total=len(data), desc=fn):
            f.write(i)

def menu():
    print("------------------------------------------")
    print("******************************************")
    print("1: Australia                              ")
    print("2: Austria                                ")
    print("3: France                                 ")
    print("4: Germany                                ")
    print("5: Hungary                                ")
    print("6: Italy                                  ")
    print("7: New Zealand                            ")
    print("8: Poland                                 ")
    print("9: Portugal                               ")
    print("10: Spain                                 ")
    print("******************************************")
    print("------------------------------------------")
    print("\n")
    v = int(input("Enter in your selection as numeric >> ").strip())
    return v


def main():
    network = 0
    try:
        r = requests.get('https://www.google.com', timeout=4)
        network = 1
    except (requests.ConnectionError, requests.Timeout):
        network = 0

    if network == 1:
        m = menu()
        if m == 1:
            pullCSV()
            v, w, x, y, z = procAut()
            writeData(v,w,x,y,z)
        elif m == 2:
            pullCSV()
            procAst()
        elif m == 3:
            pullCSV()
            procFra()
        elif m == 4:
            pullCSV()
            procDeu()
        elif m == 5:
            pullCSV()
            procHun()
        elif m == 6:
            pullCSV()
            procIta()
        elif m == 7:
            pullCSV()
            procNza()
        elif m == 8:
            pullCSV()
            procPol()
        elif m == 9:
            pullCSV()
            procPor()
        elif m == 10:
            pullCSV()
            procSpa()
        else:
            print("No available options.")
            sys.exit(1)
    else:
        print("No internet Access, Apparently.")
        sys.exit()


if __name__ == "__main__":
    main()