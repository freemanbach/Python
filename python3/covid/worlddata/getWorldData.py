#!/bin/env python3

# author        : freeman
# date          : 2021.03.05
# desc          : Add tqdm and perhaps shorten the code
# version       : 0.0.1
################################################


try:
    from tqdm import trange, tqdm
except ImportError as herr:
    print("Missing tqdm lib.")
    print("pip install --user tqdm")


try:
    from requests.exceptions import HTTPError
    import requests
except ImportError as herr:
    print("Missing requests library")
    print("pip install --user requests")


from datetime import datetime
import csv
import sys
import os.path
from os import path


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
        with open('owid-covid-data.csv', 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            for i in resp.iter_lines():
                w.writerow(i.decode('utf-8').split(','))
    except HTTPError as herr:
        print("Http Connection Error", herr)
        sys.exit()


# Fields Location: country 2, date 3, cases 4, death 7, hospitalization 19, testing 26, vaccination 34
# Fields Used: location, date, total_cases, total_deaths, hosp_patients, total_tests, total_vaccinations
def procAut():
    # https://www.geeksforgeeks.org/python-reverse-dictionary-keys-order/
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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "aut"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "ast"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "fra"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "deu"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "hun"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "ita"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "nza"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "pol"

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

    return res_dc, res_dd, res_dh, res_dt, res_dv, "por"

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
    
    return res_dc, res_dd, res_dh, res_dt, res_dv, "spa"

def writeData( a, b, c, d, e, g):
    mess = ""
    datatypes = ["case_data.csv", "death_data.csv", "hosp_data.csv", "test_data.csv", "vacc_data.csv"]
    with open (str(g+"_"+datatypes[0]), "w+") as f:
        for k, v in a.items():
            mess=str(k)+','+str(v)+"\n"
            f.write(mess)

    with open (str(g+"_"+datatypes[1]), "w+") as f:
        for k, v in b.items():
            mess=str(k)+','+str(v)+"\n"
            f.write(mess)

    with open (str(g+"_"+datatypes[2]), "w+") as f:
        for k, v in c.items():
            mess=str(k)+','+str(v)+"\n"
            f.write(mess)

    with open (str(g+"_"+datatypes[3]), "w+") as f:
        for k, v in d.items():
            mess=str(k)+','+str(v)+"\n"
            f.write(mess)

    with open (str(g+"_"+datatypes[4]), "w+") as f:
        for k, v in e.items():
            mess=str(k)+','+str(v)+"\n"
            f.write(mess)


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
        if path.exists('owid-covid-data.csv'):
            pass
        else:
            pullCSV()
        if m == 1:
            v, w, x, y, z, c = procAut()
            writeData(v,w,x,y,z,c)
        elif m == 2:
            v, w, x, y, z, c = procAst()
            writeData(v,w,x,y,z,c)
        elif m == 3:
            v, w, x, y, z, c = procFra()
            writeData(v,w,x,y,z,c)
        elif m == 4:
            v, w, x, y, z, c = procDeu()
            writeData(v,w,x,y,z,c)
        elif m == 5:
            v, w, x, y, z, c = procHun()
            writeData(v,w,x,y,z,c)
        elif m == 6:
            v, w, x, y, z, c = procIta()
            writeData(v,w,x,y,z,c)
        elif m == 7:
            v, w, x, y, z, c = procNza()
            writeData(v,w,x,y,z,c)
        elif m == 8:
            v, w, x, y, z, c = procPol()
            writeData(v,w,x,y,z,c)
        elif m == 9:
            v, w, x, y, z, c = procPor()
            writeData(v,w,x,y,z,c)
        elif m == 10:
            v, w, x, y, z, c = procSpa()
            writeData(v,w,x,y,z,c)
        else:
            print("No available options.")
            sys.exit(1)
    else:
        print("No internet Access, Apparently.")
        sys.exit()


if __name__ == "__main__":
    main()