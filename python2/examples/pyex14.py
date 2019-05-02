# Author      : freeman
# Date        : 2018.10.03
# Version     : 0.0.2
# Description : In-Class Example
#################################################

import sys
import os
import time
import random
import math

def playgame():
    play = raw_input("Want to play this guessing game: (y or n) ? ")
    if not play.strip().isdigit() or play.strip().lower() != 'n' or play.strip().lower() != 'no':
        while play.strip().lower() == "y" or play.strip().lower() == "yes":
            value = raw_input("Enter in a value inclusive (1-10): ")
            if value.isdigit():
                value = int(value.strip())
                guessMyNumber(value)
                play = raw_input("Want to play: (y or n) ? ")
                if play.strip().lower() == 'n' or play.strip().lower()=='no':
                    print "\n"
                    print "Ending Game......."
                    sys.exit(0)  # Normal Exit
                elif play.strip().isdigit():
                    print "\n"
                    print "Wrong input."
                    sys.exit(1)  # Error Exit
                else:
                    continue
            else:
                print "System doesnt accept non digits, Exiting....."
                sys.exit(1)  # Error Exiting.
    else:
        print "Exiting program since write input type: y or n only."
        sys.exit(1)       # Error Exit

def guessMyNumber(human):
    random.seed(time.time())
    pc = random.randint(1,10)

    if human < pc:
        print "Your guess is lower than PC Number." + " PC Number is:" + str(pc)
    elif human > pc:
        print "Your guess is higher than PC Number." + " PC Number is:" + str(pc)
    elif pc == human:
        print "Your have guessed Correctly." + " PC Number is:" + str(pc)
    else:
        print "Error: something is incorrect."
        sys.exit(1) # error exiting

def main():
    playgame()

main()
