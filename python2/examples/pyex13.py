# Author  : freeman
# Date    : 2019.04.13
# Version : 0.0.1
# Desc    : Program 13
#         : Obj Classes Programming-- simple inheritance example 2
###################################################################

import os
import sys
import time

# Class Object
class Customer(object):
    # Constructor
    def __init__(self, custid, name, gender):
        self.custid = custid
        self.name = name
        self.gender = gender

    def setCustID(self, custid):
        self.custid = custid

    def setName(self, name):
        self.name = name
	
    def setGender(self, gender):
        self.gender = gender

    def getCustID(self):
        return self.custid

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def toString(self):
        print "Customer ID: " + self.custid
        print "Name       : " + self.name
        print "Gender     : " + self.gender


class Account(Customer):
    # Constructor
    def __init__(self, custid, name, gender, accid, accbalance ):
        super(Customer, self).__init__()
        Customer.__init__(self, custid, name, gender )
        self.accid = str(accid)
        self.accbalance = float(accbalance)

    def setBalance(self, accbalance):
        self.accbalance = float(accbalance)

    def getBalance(self):
        return self.accbalance
    
    def getAccID(self):
        return self.accid

    def getCustID(self, accnum):
        return super(Customer, self).getCustID()

    def toString(self):
        super(Account, self).toString()
        print "Your account ID: " +  self.getAccID() 
        print "your balance   : " +  str(self.getBalance())


def main():

    jane = Account( '111' , 'Jane silver', 'f', '111222', 200000)
    print ""
    jane.toString()
    jane.getBalance()

if __name__ == "__main__":
    main()
