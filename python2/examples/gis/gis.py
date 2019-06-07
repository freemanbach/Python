#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.06.04
# Version : 0.0.1
# Desc    : sample test file for GIS
#         : 
#         : You have to get a Google Cloud Console key with you google account and
#         : enabled geolocation, Geocoding, places.
#         : Google wants your Credit card info, otherwise you can
#         : only pull 1 request per DAY.
###################################################################


import warnings
import sys
import requests


def main():
    api_key="---YOUR GOOGLE PROJECT CREDENTIAL KEY---"
    loc = "Harvard University"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc + "&" + "key=" + api_key
    r = requests.get(url)
    data = r.json()
    print data



if __name__ == "__main__":
    main()
