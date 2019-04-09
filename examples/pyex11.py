# Author  : freeman
# Date    : 2019.04.09
# Version : 0.0.1
# Desc    : Program 11
#         : python Error handling -- simple Error handling example
###################################################################

import os
import sys

def test():
    mylst = [ 'b', 0, 2 ]
    for i in mylst:
        try:
            print "The value is: " + str(i)
            r = float(1.00 / int(i))
            break
        except:
            print "Error: " + str(sys.exc_info()[0]) + " happened."
            print "Trying next value"

    print "The remainder of: " + str(i) + " " + " is " + str(r)

def main():
    test()


if __name__ == "__main__":
    main()
