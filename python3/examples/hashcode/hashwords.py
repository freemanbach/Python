#!/usr/bin/env python3

"""
Author    : Freeman
Date      : 2020.03.03
version   : 0.0.1  
Desc      : hasing the entire english word into sha1, sha256, sha384
wordSrc   : https://github.com/dwyl/english-words
use       : python3 hashword.py words_alpha.txt
"""


import hashlib  # main hashing libs 
import hmac     # message algorithm
import zlib     # adler and crc32
import sys


def processwords():
    """ return each words from file as a list. """
    
    size = len(sys.argv)
    words, fn = [], ""
    
    if size != 2:
        print("Supply the dictionary file, words_alpha.txt. ")
        sys.exit(0)
    else:
        fn = sys.argv[1]

    with open(fn, mode='r') as wf:
        for i in wf:
            i = i.strip()
            i = str(i)
            words.append(i)
            
    return words


def processhash(mylst):
    """ prints the hashed values to screen. """ 
    hashword, tmp = dict(), []
    
    for i in mylst:
        a = str(i)
        h_sha1 = hashlib.sha1(a.encode('utf-8')).hexdigest()
        h_sha256 = hashlib.sha256(a.encode('utf-8')).hexdigest()
        h_sha384 = hashlib.sha384(a.encode('utf-8')).hexdigest()
        # left this out intentionally
        #h_sha512 = hashlib.sha512(i.encode('utf-8')).hexdigest()
        hashword.update( { i : [h_sha1, h_sha256, h_sha384 ] } )
    
    # Printing out the hashes(sha1, sha384, sha512) for each word
    # from the word file, you can also add h_sha512 to the list
    for i, k in hashword.items():
        print( i, "  " , k )

    
def main():
    a = processwords()
    processhash(a)
    
    
if __name__ == '__main__':
    main()