# Author  : freeman
# Date    : 2018.11.19
# Version : 0.0.1
# Desc    : Program 6
#         : Obj Classes Programming
###################################################################

import os
import sys
import time

# Class Object
class Account:
    # Constructor
    def __init__(self, name, addr, ssn, dob):
        self.name = name
        self.addr= addr
        self.ssn= ssn
        self.dob= dob


    def setName(self, name):
        self.name = name
	

    def setAddr(self, addr):
        self.addr = addr


    def setSSN(self, ssn):
        self.ssn= ssn 


    def setDOB(self, dob):
        self.dob= dob 

	
    def getName(self):
        return self.name


    def getAddr(self):
        return self.addr


    def getSSN(self):
        return self.ssn


    def getDOB(self):
        return self.dob
    

    def toString(self):
        print "Name  is: " + self.name
        print "Address is: " + self.addr
        print "SSN is: " + self.ssn 
        print "DOB is: " + self.dob


# Class Checking
class Checking(Account):
    # Constructor
    def __init__(self, name, addr, ssn, dob, accamt, accnum):
        Account.__init__(self, name, addr, ssn, dob)
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
        print "Your account info is: " + self.getName() + " " + self.getAddr() + " " + self.getSSN() + " " + self.getDOB()


def main():

    joe = Checking("joe","20 hobbit court", "111-23-3456", "02/12/1945",56.9, "VA111233456")
    joe.toString()


if __name__ == "__main__":
    main()
