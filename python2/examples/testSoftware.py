#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.15
# Version : 0.0.3
# Desc    : Testing Availability of 6 Packages
#         : 
###################################################################


import sys


try:
    import json
    print "You have JSON installed!"
except ImportError as err:
    print "You dont have JSON installed."
    print err.__class__.__name__ + ": " + err.message
    #sys.exit(1)


try:
    from bs4 import BeautifulSoup
    print "You have BS4 installed !"
except ImportError as err:
    print "You dont have BeautifulSoup installed."
    print err.__class__.__name__ + ": " + err.message
    #sys.exit(1)


try:
    import requests
    print "You have Requests installed !"
except ImportError as err:
    print "You dont have Requests installed."
    print err.__class__.__name__ + ": " + err.message
    #sys.exit(1)


try:
    import scrapy
    print "You have Scrapy installed !"
except ImportError as err:
    print "You dont have Scrapy installed."
    print err.__class__.__name__ + ": " + err.message
    #sys.exit(1)


try:
    import sqlite3
    print "You have SQlite3 installed !"
except ImportError as err:
    print "You dont have Sqlite3 installed."
    print err.__class__.__name__ + " : " + err.message
    #sys.exit(1)


try:
    import pandas as pd
    print "You have pandas installed !"
except ImportError as err:
    print "You dont have pandas installed."
    print err.__class__.__name__ + " : " + err.message
    #sys.exit(1)


try:
    import PyPDF2
    print "You have Python Pdf Reader installed !"
except ImportError as err:
    print "You dont have Python Pdf Reader installed."
    print err.__class__.__name__ + " : " + err.message
    #sys.exit(1)


def main():
    return 0


if __name__ == "__main__":
    main()
