# Author  : freeman
# Date    : 2018.11.19
# Version : 0.0.1
# Desc    : Program 6
#         : Obj Classes Programming-- Complex inheritance example
###################################################################

import os
import sys
import time

# Class Object
class Account(object):
    # Constructor
    def __init__(self, name, addrnum, addrname, addrcity, addrstate, addrzip, ssn, dob):
        self.name = name
        self.addrnum= addrnum
        self.addrname= addrname
        self.addrcity= addrcity
        self.addrstate= addrstate
        self.addrzip= addrzip
        self.ssn= ssn
        self.dob= dob

    def setName(self, name):
        self.name = name
	
    def setAddrNum(self, addrnum):
        self.addrnum = addrnum

    def setAddrName(self, addrname):
        self.addrname = addrname

    def setAddrCity(self, addrcity):
        self.addrcity = addrcity

    def setAddrState(self, addrstate):
        self.addrstate = addrstate

    def setAddrZip(self, addrzip):
        self.addrzip = addrzip

    def setSSN(self, ssn):
        self.ssn= ssn 

    def setDOB(self, dob):
        self.dob= dob 

    def getName(self):
        return self.name

    def getAddrNum(self):
        return self.addrnum

    def getAddrName(self):
        return self.addrname

    def getAddrCity(self):
        return self.addrcity

    def getAddrState(self):
        return self.addrstate

    def getAddrZip(self):
        return self.addrzip

    def getSSN(self):
        return self.ssn

    def getDOB(self):
        return self.dob
    
    def toString(self):
        print "Name  is: " + self.name
        print "Address is: " + self.addrnum + " " + self.addrname + " " + self.addrcity + " " + self.addrstate + " " + self.addrzip
        print "SSN is: " + self.ssn 
        print "DOB is: " + self.dob


# Class Checking
class Checking(Account):
    # Constructor
    def __init__(self, name, addrnum, addrname, addrcity, addrstate, addrzip, ssn, dob, accamt, accnum):
        super(Account, self).__init__()
        Account.__init__(self, name, addrnum, addrname, addrcity, addrstate, addrzip, ssn, dob)
        self.accamt = float(accamt)
        self.accnum = accnum

    def setAccAmt(self, accamt):
        self.accamt = float(accamt)

    def getAccNum(self):
        return self.accnum
    
    def getAccAmt(self):
        return self.accamt

    def setAccNum(self, accnum):
        self.accnum = accnum

    def toString(self):
        super(Checking, self).toString()
        print "Your account info is: " +  " " + self.getAccNum()  + " " + str(self.getAccAmt())


def main():

    joe = Checking("joe","20",  "hobbit court", "hobbitsburg", "va", "24073", "111-23-3456", "02/12/1945", 10000000.99, "VA111233456")
    joe.toString()


if __name__ == "__main__":
    main()
