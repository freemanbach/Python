#!/usr/bin/env python3

"""
Author    : Freeman
Date      : 2020.03.04
version   : 0.0.2
Desc      : using wordSrc2 to generate four categories of one monolithic file for each categories
          : inorder to make a pass-phrase password generator.
wordSrc1  : https://github.com/StevensDeptECE/Dictionaries
wordSrc2  : http://www.ashley-bovan.co.uk/words/partsofspeech.html
use       : python3 choosePasswd.py file1.txt file2.txt file3.txt file4.txt etc.........
"""


import sys
import os
import os.path
from os import path


# phase 1 to combine all the words together into a single file 
# of each part of speech without overlapping words for each categories
def processadv():
    
    fns, cnt, file_words, fData = [], 0, set(), []
    
    if path.exists('advoutput.txt'):
        os.remove('advoutput.txt')
    
    a = len(sys.argv)
    f = open("advoutput.txt", "a+")
    
    if a < 2:
        print("Need at minimum one file to process like-terms.")
        print("run: python3 choosePasswd.py filename1.txt filename2 ...")
        sys.exit()
    else:
        while cnt < a:
            fns.append(sys.argv[cnt])
            cnt+=1
    
    # remove the first item of this list
    fns.pop(0)
    
    # Process all the files in each directories into one giant list
    for i in range(0, len(fns)):
        with open( fns[i], mode='r' ) as fn:
            for i in fn:
                tmp = str(i).strip()
                if "'" in tmp:
                    tmp = ""
                else:
                    file_words.add(tmp)
    
    # Sorting the words alfabetically
    fData = sorted(file_words)
    
    for i in fData:
        f.write(i+"\n")
    f.close()
    
    print("Done processing adverbs.")        

    
def main():
    #processverb()
    #processadj()
    processadv()
    #processnoun()
    
    
if __name__ == "__main__":
    main()