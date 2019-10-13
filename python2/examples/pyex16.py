# Author  : freeman
# Date    : 2019.10.13
# Version : 0.0.1
# Desc    : Example 3
#
###################################################################

import time
import random
import sys
import math
import string

"""
-- Must prompt the user for number of lowercase and number of uppercase characters
-- Must prompt the user for number of digits and number of special characters 
-- Also, prompt the user of the number of passwords they wish to display on the screen.
-- You must then display no more than 5 pseudo randomly generated pwords per line
-- Everything must coincide the length requirement, if a user wanted 18 lower and upper character and the max is only 16, you have to decide what to do !
-- At least 2 letter between [a-z] and 2 letter between [A-Z].
-- At least 1 number between [0-9].
-- At least 1 character from [!@#$%^&*?()<>/\|]; no period, semi or colons, brackes, or even braces
-- Minimum length 6 characters.
-- Maximum length 16 characters.

"""

def genPword(lca, uca, da, pa):
    random.seed(time.time())
    lc = string.letters[:26]
    uc = string.letters[26:]
    dts = string.digits
    punt = string.punctuation[:5]
    cnt = 0
    pword = ""
    for i in range(0, lca):
        pword+=str(random.choice(lc))
    for i in range(0, uca):
        pword+=str(random.choice(uc))
    for i in range(0, da):
        pword+=str(random.choice(dts))
    for i in range(0, pa):
        pword+=str(random.choice(punt))

    return pword
    

def password():

    lcc = input("Enter number of lowercase Characters? ")
    ucc = input("Enter number of uppercase Characters? ")
    dt = input("Enter the number of digits ? ")
    pun = input("Enter the number of punctuations ? ")
    nop = input("Number of passwords? ")
    cnt = 0
    pwords = []
    
    if lcc + ucc + dt + pun >= 6 and lcc + ucc + dt + pun <= 16:
        while cnt < nop:
            tmp = genPword(lcc, ucc, dt, pun)
            pwords.append(tmp)
            cnt+=1
            
        for i in pwords:
            print i
    else:
        print "Password size must be longer than 6 and smaller than 16 in length."
        sys.exit(0)
        
    return 0


def main():
    password()
    return 0
 

if __name__ == "__main__":
    main()
