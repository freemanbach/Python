#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.15
# Version : 0.0.1
# Desc    : Testing Availability of 3 Packages
#         : 
###################################################################


import sys


try:
    from bs4 import BeautifulSoup
    print "You have BS4 installed !"
except ImportError as err:
    print "You dont have BeautifulSoup installed."
    print err.__class__.__name__ + ": " + err.message
    sys.exit(1)


try:
    import requests
    print "You have Requests installed !"
except ImportError as err:
    print "You dont have Requests installed."
    print err.__class__.__name__ + ": " + err.message
    sys.exit(1)


try:
    import scrapy
    print "You have Scrapy installed !"
except ImportError as err:
    print "You dont have Scrapy installed."
    print err.__class__.__name__ + ": " + err.message
    sys.exit(1)
