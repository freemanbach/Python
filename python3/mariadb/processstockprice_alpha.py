#!/bin/env python3

import sys

"""
author     : freeman
date       : 20200102
desc       : Process Alpha Vantage Stock Data into sql for our stock_price table
           : 
use        : python3 processstockprice_alpha.py STOCK_SYMBOL.csv sp_data.sql
use        : python3 processstockprice_alpha.py daily_goog.csv sp_data.sql
           :
DATA       : https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=YOUR_PERSONAL_API_KEY&datatype=csv
           : 
README     : First download the CSV file using your web-browser, copy and paste the URL link to your browser, 
           : There should now be a file called daily_STOCK_SYMBOL.csv in your download directory. 
           : Then run this python script to generate the single line of sql as in sp_data.sql file. 
           : Then, run this sp_data.sql file on your prompt to populate your DB.
MYSQL_CMD  : mysql -u YOUR_USER_NAME -p < sp_data.sql

Idea       : select max(id) from tablename;
"""

#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=IP471WT33VI5XIGY&datatype=csv 
def processdata(ifile, ofile):
    sql = []
    with open(ifile, 'r') as f:
        for i in f:
            a = i.split(',')
            tmp = "INSERT INTO stock_price (ticker_id, date, open, high, low, close, volume) VALUES" \
            "("   + str(1) + ',' + "\'" + str(a[0]).strip() + "\'" +  ","   \
                  + str(a[1]).strip() +  ","   \
                  + str(a[2]).strip() +  ","   \
                  + str(a[3]).strip() +  ","   \
                  + str(a[4]).strip() +  ","   \
                  + str(a[5]).strip("\n") +  ");\n"  
            sql.append(tmp)
            tmp = ""
    sql.pop(0)
    sql.reverse()
    sql.insert(0, "use simplefinance;\n")
    print(sql)
    with open(ofile, 'w') as f:
        for i in sql:
            f.write(i)
    

def main():
    if len(sys.argv) == 3:
        dfile = sys.argv[1]
        ofile = sys.argv[2]
        processdata(str(dfile), str(ofile))
    elif len(sys.argv) == 2:
        print("ok, we will make this sp_data.sql file for you.")
        dfile = sys.argv[1]
        ofile = "sp_data.sql"
        processdata(str(dfile).strip(), str(ofile))
    else:
        print("idk, Not enough parameters ?!?!?!")
        print("See File Header !")


if __name__ == "__main__":
    main()