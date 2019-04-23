#!/usr/bin/env python
# Author  : freeman
# Date    : 2018.11.16
# Version : 0.0.1
# Desc    : Program 4
#         : Decision making
###################################################################

import os
import sys
import time


def main():
    
    # let us if we want to buy a dell, HP, ASUS or apple laptop
    print "To view our inventory, Enter in the name of the brand."
    print "The Following will display specs and price for each brand of laptop."
    ui = raw_input("Enter in dell, hp, asus, or apple>>> ")
    print "\n"

    # matching the correct brand with price, OS, RAM, HD and CPU
    if ui.strip().lower() == "dell":
        print "--8th Gen Intel Core i3-8130U"
        print "--Windows 10 Pro"
        print "--8GB, 1x8GB"
        print "--2.5\" 500GB SATA 7200 RPM Hard Drive" 
        print "--$799.00"
        print ""
    elif ui.strip().lower() == "hp":
        print "--Intel Core i5-8250U (1.6 GHz)"
        print "--8 GB LPDDR3-2133 SDRAM (onboard)"
        print "--258 GB PCIe NVMe M.2 SSD"
        print "--Windows 10 Pro"
        print "--$999.00"
        print ""
    elif ui.strip().lower() == "asus":
        print "--Intel Core i9-8950HK processor"
        print "--Windows 10 Pro"
        print "--8GB / 16GB 2400MHz DDR4 onboard"
        print "--512GB / 256GB SATA3 SSD"
        print "--$2299.99"
        print ""
    elif ui.strip().lower() == "apple":
        print "--2.3GHz dual-core Intel Core i5, Turbo Boost"
        print "--128GB SSD"
        print "--MAC OS Mojave"
        print "--8GB of 2133MHz LPDDR3 onboard memory"
        print "--$1299"
        print ""
    else:
        print "There are no brands in our inventory!"
        sys.exit(1)


if __name__ == "__main__":
    main()
