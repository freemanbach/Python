#!/bin/env python3

"""
author     : freeman
date       : 20200102
desc       : Process Alpha Vantage Stock Data into sql for our company table
           : 
use        : python3 processcompany_alpha.py Stock_Symbol.json com_data.sql
use        : python3 processcompany_alpha.py ibm.json com_data.sql
           :
DATA       : https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=YOUR_PERSONAL_API_KEY
           : 
READ       : First download the JSON file using your web-browser, copy and paste the json data onto a
           : text editor and save the file as STOCK_SYMBOL.json as shown in the use area. 
           : Then run this python script to generate the single line of sql as in data.sql file. 
           : mysql -u YOUR_USER_NAME -p < com_data.sql
"""


import sys
import random
import json

def processdata(infile, otfile):
    sql, a = [], ""
    with open(infile, 'r') as jf:
        data = json.load(jf)
    z = str(data['Description']).strip()
    z = z.replace("'", "")
    a = "INSERT INTO company (ticker, assettype, name, description, exchange,currency ,country ,sector ,industry ) VALUES" \
             "(" + "\'" +str(data['Symbol']).strip() + "\'" +  ","   \
                + "\'" + str(data['AssetType']).strip() + "\'" + "," \
                + "\'" + str(data['Name']).strip() + "\'" + "," \
                + "\'" + z + "\'" + "," \
                + "\'" + str(data['Exchange']).strip() + "\'" + "," \
                + "\'" + str(data['Currency']).strip() + "\'" + "," \
                + "\'" + str(data['Country']).strip() + "\'" + "," \
                + "\'" + str(data['Sector']).strip() + "\'" + "," \
                + "\'" + str(data['Industry']).strip() + "\'"  ");" + "\n" 
    sql.append("use simplefinance;\n")
    sql.append(a)
    print(sql)
    
    with open(otfile, 'w') as f:
        for i in sql:
            f.write(i)


def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        outfile = sys.argv[2]
        processdata(str(filename).strip(), str(outfile).strip())
    elif len(sys.argv) == 2:
        print("ok, we will make this com_data.sql file for you.")
        filename = sys.argv[1]
        outfile = "com_data.sql"
        processdata(str(filename).strip(), str(outfile))
    else:
        print("idk, Not enough parameters ?!?!?!")
        print("See File Header !")

if __name__ == "__main__":
    main()