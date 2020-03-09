#!/usr/bin/env python3

"""
Author    : Freeman
Date      : 2020.03.03
version   : 0.0.1  
Desc      : hasing the entire english word into sha1, sha256, sha384
wordSrc   : https://github.com/dwyl/english-words
use       : python3 hashwords.py words_alpha.txt
"""


import hashlib  # main hashing libs 
import json     # import Json
import sys


def processwords():
    """ return each words from file as a list. """
    
    size = len(sys.argv)
    words, fn = [], ""
    
    if size != 2:
        print("Argument File Not Found.                      ")
        print("Supply the dictionary file, words_alpha.txt.  ")
        print("run:   python3 hashwords.py words_alpha.txt.  ")
        sys.exit(0)
    else:
        fn = sys.argv[1]

    with open(fn, mode='r') as wf:
        for i in wf:
            i = i.strip()
            i = str(i)
            words.append(i)
            
    return words

"""
data = {}
data['vocabs'] = []
data['vocabs'].append( { 'word': v[0], 'sha1': v[1], 'sha256': v[2]  } )
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
 
"""
def processhash(mylst):
    """ prints the hashed values to screen. """ 
    hashword, tmp = dict(), []
    
    for i in mylst:
        a = str(i)
        h_sha1 = hashlib.sha1(a.encode('utf-8')).hexdigest()
        h_sha256 = hashlib.sha256(a.encode('utf-8')).hexdigest()
        h_sha384 = hashlib.sha384(a.encode('utf-8')).hexdigest()
        # left this out intentionally
        # h_sha512 = hashlib.sha512(a.encode('utf-8')).hexdigest()
        hashword.update( { i : [ h_sha1, h_sha256, h_sha384 ] } )
    
    # Printing out the hashes(sha1, sha384, sha512) for each word
    # from the word file, you can also add h_sha512 to the list
    #for k, v in hashword.items():
    #    print( k, "  " , v[0] )
    createJson(hashword)
    

def createJson(ddict):
    jdata = {}
    jdata['vocabs'] = []
    for k, v in ddict.items():
        jdata['vocabs'].append( { 'word': str(k), 'sha1': str(v[0]), 'sha256': str(v[1]),'sha384': str(v[2]) } )
    jd = json.dumps(jdata, sort_keys=False, indent=4)
    print(jd)

    
def main():
    a = processwords()
    processhash(a)
    
    
if __name__ == '__main__':
    main()