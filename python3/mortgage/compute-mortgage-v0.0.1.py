#!/usr/bin/env python3
"""
Author  : flo
date    : 2022.08.08
Purpose : example of finding out the amount of principle paid to mortgage lender per year.
        : This version is uniquely special.

Comments: Simulate the number of mortgage payments based on the loan amount.
        : run the example command to first see how it needs to run.
        : Getopt is interesting to use, short and long parameters in function do worked.
Version : 0.0.1

example : python3 compute-mortgage-v0.0.1.py -h
example : python3 compute-mortgage-v0.0.1.py -v
"""

import getopt
import sys
import datetime
import calendar

def computeMortgage(tot, mon, rate, intr, pal, m, y):

    if m != "" and y != "":
        currentMonth = int(m)
        currentYear = int(y)
    else:
        sys.exit(1)

    mtsum = 0.00

    for i in range(1, mon+1):
        daysInMonth = calendar.monthrange(currentYear, currentMonth)[1]
        for x in range(1, daysInMonth+1):
            tsum = tot * (rate/100.00) * (1.00/365.00)
            mtsum += tsum
            tot = tsum + tot

            if x < 10:
                dvalue = "0" + str(x)
            else:
                dvalue = str(x)

            if currentMonth < 10:
                mvalue = "0" + str(currentMonth)
            else:
                mvalue = str(currentMonth)
            print(" Year " + str(currentYear) + " Month " + str(mvalue) + " Day  " + str(dvalue) + "      " + \
                  format(tot, '.4f') + "      " + format(tsum, '.4f'))
        if currentMonth == 12:
            currentYear += 1
            currentMonth = 1
        else:
            currentMonth += 1
        tot = tot - (pal + intr)
        print(" Actual Uptodate Interests Paid:               " + format(mtsum, '.4f'))


def version():

    print("version 0.0.1")


def usage():

    usage = """
            usage: python3 compute-mortgage-v0.0.1.py [-l,--la = Float_VALUE]   [-t,--lt = Integer_VALUE] [-r,--lr = Float_VALUE  ] 
                                                      [-i,--li = Float_VALUE]   [-p,--lp = Float_VALUE  ] [-m,--cm = Integer_VALUE] 
                                                      [-y,--cy = Integer_VALUE] [-h] [-v]
            examples:
            python3 compute-mortgage-v0.0.1.py
            python3 compute-mortgage-v0.0.1.py -l 250000.99 -t 24 -r 4.95 -i 515.69 -p 600 -m 2 -y 2000
            python3 compute-mortgage-v0.0.1.py -l 250000.99 -t 24 -r 4.95 -i 0 -p 0 -m 2 -y 2000
            python3 compute-mortgage-v0.0.1.py -l 250000.99 -t 24 -r 4.95 -i 0 -p 0
            *python3 compute-mortgage-v0.0.1.py -l 250000.99 -t 12x5 -r 4.95 -i 0 -p 0 -m 2 -y 2000
            python3 compute-mortgage-v0.0.1.py --la 250000.99 --lt 24 --lr 4.95 --li 515.69 --lp 600 --cm 2 --cy 2000
            python3 compute-mortgage-v0.0.1.py --la=250000.99 --lt=24 --lr=4.95 --li=515.69 --lp=600 --cm=2 --cy=2000

            python compute-mortgage-v0.0.1.py -v
            python compute-mortgage-v0.0.1.py -h

            options :
            -l, --la=value, --la value  take a loan Value amount
            -t, --lt=value, --lt value  take an actual or a hypothetical value term
            -r, --lr=value, --lr value  take the monthly interests value rate
            -i, --li=value, --li value  take the monthly interests value amount
            -p, --lp=value, --lp value  take the monthly principle value amount
            -m, --cm=value, --cm value  take a Custom Month value
            -y, --cy=value, --cy value  take a Custom Year value
            -v                          show program's version number and exit
            -h                          show this help message and exit
            """

    print(usage)


def main():

    # default values
    now = datetime.datetime.now()
    lamt, lterm, lrate, lint, lprin, lcm, lcy = 200000.99, 10, 3.89, 450, 600.99, now.month, now.year

    # try the getopt function for kicks and giggles
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'l:t:r:i:p:m:y:vh', ['la=', 'lt=', 'lr=', 'li=', 'lp=', 'cm=', 'cy='])
    except getopt.GetoptError as err:
        # print something and exit
        print(str(err))
        usage()
        sys.exit(2)

    # pull data from getopt
    for o, a in opts:
        if o in ('-l', '--la'):
            if a.replace('.','',1).isdigit():
                lamt = float(a)
            else:
                print("Please enter your loan amount in digit form. ")
                sys.exit(2)
        elif o in ('-t', '--lt'):
            lts = []
            if a.isdigit():
                lterm = int(a)
            elif a.isalnum():
                lts = a.split('x')
                lterm = int(lts[0]) * int(lts[1])
            else:
                print("Please enter your loan duration in digit form. ")
                sys.exit(2)
        elif o in ('-r', '--lr'):
            if a.replace('.','',1).isdigit():
                lrate = float(a)
            else:
                print("Please enter your loan rate in digit form. ")
                sys.exit(2)
        elif o in ('-i', '--li'):
            if a.replace('.','',1).isdigit():
                lint = float(a)
            else:
                print("Please enter your loan accrual monthly interests in digit form. ")
                sys.exit(2)
        elif o in ('-p', '--lp'):
            if a.replace('.','',1).isdigit():
                lprin = float(a)
            else:
                print("Please enter your loan accrual monthly principle in digit form. ")
                sys.exit(2)
        elif o in ('-m', '--cm'):
            if a.replace('.', '', 1).isdigit():
                lcm = int(a)
            else:
                print("Please enter your Custom Month. ")
                sys.exit(2)
        elif o in ('-y', '--cy'):
            if a.replace('.', '', 1).isdigit():
                lcy = int(a)
            else:
                print("Please enter your Custom Year. ")
                sys.exit(2)
        elif o in ('-v', '--version'):
            version()
            sys.exit()
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    # compute and forecast it all
    computeMortgage(lamt, lterm, lrate, lint, lprin, lcm, lcy)

# calling main
if __name__ == "__main__":
    main()
