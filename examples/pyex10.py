# Author  : freeman
# Date    : 2019.04.09
# Version : 0.0.1
# Desc    : Program 10
#         : python OO programming -- simple inheritance example
###################################################################

import os
import sys
import time

class Car:
    # Global variable
    car = "Honda"

    def __init__(self):
        # private data members
        self.__carprice = 25999.99
        self.__carbrand = "Honda"
        self.__carspeed = "fast"
        self.__milagePG = 32

    def price(self):
        print "Selling price: {}".format(self.__carprice)

    def setSellPrice(self, price):
        self.__carprice = price

    def brand(self):
        print "Car brand    : {}".format(self.__carbrand)

    def setBrand(self, brand):
        self.__carbrand = brand

# let there be main
def main():
    car = Car()
    car.price()
    car.brand()
    car.setSellPrice(200000)
    car.setBrand("Ferrari")
    car.price()
    car.brand()


if __name__ == "__main__":
    main()
