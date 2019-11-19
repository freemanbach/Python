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
        self.carprice = 0.00
        self.carbrand = ""
        self.carspeed = 0.00
        self.milagePG = 0.00

    def getSellPrice(self):
        print "Selling price: {}".format(self.carprice)

    def setSellPrice(self, price):
        self.carprice = price

    def getCarBrand(self):
        print "Car brand    : {}".format(self.carbrand)

    def setCarBrand(self, brand):
        self.carbrand = brand

    def getCarSpeed(self):
        print "Car speed    : {}".format(self.carspeed)

    def setCarSpeed(self, speed):
        self.carspeed = speed
        
    def getCarMilage(self):
        print "Car milage Per Gallon   : {}".format(self.milagePG)

    def setCarMilage(self, miles):
        self.milagePG = miles


        
# let there be main
def main():
    car = Car()
    car.getSellPrice()
    car.getCarBrand()
    car.setSellPrice(200000)
    car.setCarBrand("Ferrari")
    car.getSellPrice()
    car.getCarBrand()
    gm = Car()
    gm.setSellPrice(45000)
    gm.setCarBrand("GM Truck")
    gm.getSellPrice()
    gm.getCarBrand()
    gm.setSellPrice(60000)
    gm.getSellPrice()
    toyota = Car()
    toyota.setSellPrice(50000)
    toyota.setCarBrand("Toyota")
    toyota.getSellPrice()
    toyota.getCarBrand()


if __name__ == "__main__":
    main()
