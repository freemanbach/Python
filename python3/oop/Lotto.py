# Author  : freeman
# Date    : 2020.05.21
# Version : 0.0.1
# Desc    : python OO programming example
#         :
#         : 
###################################################################

from numpy import random
import math
import sys

class Lotto:
    
    # Global Data Members
    lotto = list()
    rnum = 0

    # default Constructor w/obj data members
    def __init__(self):
        self.lotto = list()
        self.rnum = 0
        
    def additemstolist(self, size):
        for i in list(range(size)):
            self.lotto = []
            for i in list(range(6)):
                if (i==5):
                    self.rnum = self.genmagicnum()
                    self.lotto.append(self.rnum)
                else:
                    self.rnum = self.genrandnum()
                    self.lotto.append(self.rnum)
            print(self.lotto);
        
    def genrandnum(self):
        return random.randint(70)+1
    
    def genmagicnum(self):
        return random.randint(25)+1
        
        
def main():
    
    ticket = Lotto() 
    z = input("Enter in the number of Tickets: ")
    if z.isdigit():
        ticket.additemstolist(int(z))
    else:
        print("User input is not of integer value. ")
        print("Exiting............................ ")
        sys.exit()
        
    
if __name__ == "__main__":
    main()