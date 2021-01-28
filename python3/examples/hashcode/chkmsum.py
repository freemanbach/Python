#!/usr/bin/env python3


"""
Author  :  freeman
date    :  2020.03.16
Purpose :  To hash many files in the smae directory or files from other directories 
        :  with static full path.
Comments:  cant seem to add this multi file hashing into chksum.py 
        :  so this is the one file to rule that multi file hashing
"""


import os
import sys
import hashlib  # main hashing libs 
import hmac     # message algorithm
import zlib     # adler and crc32


try:
    import getopt   # parameter package lib
except ImportError as err:
    print("Missing GetOpt Library !")
    sys.exit(1)


def md5(fname):
    """ https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def sha1(fname):
    """ """
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()


def sha224(fname):
    """ """
    hash_sha224 = hashlib.sha224()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha224.update(chunk)
    return hash_sha224.hexdigest()


def sha256(fname):
    """ """
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def sha384(fname):
    """ """
    hash_sha384 = hashlib.sha384()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha384.update(chunk)
    return hash_sha384.hexdigest()


def sha512(fname):
    """ """
    hash_sha512 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
    return hash_sha512.hexdigest()


def sha3_224(fname):
    """ """
    hash_sha3_224 = hashlib.sha3_224()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_224.update(chunk)
    return hash_sha3_224.hexdigest()


def sha3_256(fname):
    """ """
    hash_sha3_256 = hashlib.sha3_256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_256.update(chunk)
    return hash_sha3_256.hexdigest()


def sha3_384(fname):
    """ """
    hash_sha3_384 = hashlib.sha3_384()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_384.update(chunk)
    return hash_sha3_384.hexdigest()


def sha3_512(fname):
    """ """
    hash_sha3_512 = hashlib.sha3_512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_512.update(chunk)
    return hash_sha3_512.hexdigest()


def shake_128(fname):
    """ the parameter in the function *.hexdigest() is the size of the return digest. 
        the length of the return digest could vary but 46 should be sufficient.  """
    hash_shake_128 = hashlib.shake_128()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_shake_128.update(chunk)
    return hash_shake_128.hexdigest(46)


def shake_256(fname):
    """ the parameter in the function *.hexdigest() is the size of the return digest. 
        the length of the return digest could vary but 46 should be sufficient.  """
    hash_shake_256 = hashlib.shake_256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_shake_256.update(chunk)
    return hash_shake_256.hexdigest(46)


def b2b(fname):
    """ """
    hash_b2b = hashlib.blake2b()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_b2b.update(chunk)
    return hash_b2b.hexdigest()


def b2s(fname):
    """ """
    hash_b2s = hashlib.blake2s()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_b2s.update(chunk)
    return hash_b2s.hexdigest()


def crc(fname):
    """ """
    with open(fname, 'rb') as f:
        buf = f.read()
    nbuf = ( zlib.crc32(buf) & 0xffffffff)
    return "%08X" % nbuf


def version():
    """ """
    print("version 0.0.1")


def chksumtypes():
    """ """
    print("Available Algorithms: ")
    hashalgor = []
    for i in hashlib.algorithms_guaranteed:
        hashalgor.append(i)
    d = hashalgor.index('blake2b')
    hashalgor.pop(d)
    d = hashalgor.index('blake2s')
    hashalgor.pop(d)
    hashalgor.append('b2b')
    hashalgor.append('b2s')
    hashalgor.append('crc')
    print("" + str(sorted(hashalgor)))


def getDataSum(atype, filelist):
    """ """
    if atype == "md5":
        for i in filelist:
            chksum = md5(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha1":
        for i in filelist:
            chksum = sha1(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha224":
        for i in filelist:
            chksum = sha224(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha256":
        for i in filelist:
            chksum = sha256(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha384":
        for i in filelist:
            chksum = sha384(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha512":
        for i in filelist:
            chksum = sha512(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha3_224":
        for i in filelist:
            chksum = sha3_224(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha3_256":
        for i in filelist:
            chksum = sha3_256(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha3_384":
        for i in filelist:
            chksum = sha3_384(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "sha3_512":
        for i in filelist:
            chksum = sha3_512(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "shake_128":
        for i in filelist:
            chksum = shake_128(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "shake_256":
        for i in filelist:
            chksum = shake_256(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "b2b":
        for i in filelist:
            chksum = b2b(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "b2s":
        for i in filelist:
            chksum = b2s(i)
            print(str(chksum) + "\t" + "*" + str(i))
    elif atype == "crc":
        for i in filelist:
            chksum = crc(i)
            print(str(chksum) + "\t" + "*" + str(i))    
    else:
        print("There is no other option ! ")
        sys.exit(1)

        
def usage():
    """ Help info """
    usage = """
            usage: python chkmsum.py [-t ,--tp = checksum_algorithm] { file1 file2 file3 file_N ...... }
                                                       [ -h ] [ -v ]
			
            examples:
            python chkmsum.py -t sha1 linux.iso 
            python chkmsum.py -t sha1 linux.iso file2.txt file3.exe file4.pdf file5.doc file6.docx file7.xls
                                      
            python chkmsum.py -v
            python chkmsum.py -h

            options :
            -t, --tp=value, --tp value  Collision Algorithms { md5:sha1:sha224:sha256:sha384:sha512:sha3_224:
                                                               sha3_256:sha3_384:sha3_512:shake_128:shake_256:
                                                               b2b:b2s:crc }
                                                               
            -v                          show program's version number and exit
            -h                          show this help message and exit
            """

    print(usage)
    
    
def main():
    """ Feel the main """
    # default values
    tp, flist = "", []

    # using getopt function for giggles only
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:vh', ['tp='])
    except getopt.GetoptError as err:
        # print something and exit
        print(str(err))
        usage()
        sys.exit(2)

    # pull data from getopt
    for o, a in opts:
        if o in ('-t', '--tp'):
            if a.strip().lower() == "md5":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha1":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha224":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha256":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha384":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha512":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha3_224":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha3_256":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha3_384":
                tp = a.strip().lower()
            elif a.strip().lower() == "sha3_512":
                tp = a.strip().lower()
            elif a.strip().lower() == "shake_128":
                tp = a.strip().lower()
            elif a.strip().lower() == "shake_256":
                tp = a.strip().lower()
            elif a.strip().lower() == "b2b":
                tp = a.strip().lower()
            elif a.strip().lower() == "b2s":
                tp = a.strip().lower()
            elif a.strip().lower() == "crc":
                tp = a.strip().lower()
            else:
                print("Please enter the limited correct type of file Collision Algorithm available to you. ")
                chksumtypes()
                sys.exit(2)
        elif o in ('-v', '--version'):
            version()
            sys.exit()
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('', ''):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"
            sys.exit(1)

    # the brain of the operation, yodaheim
    if len(sys.argv) > 3:
        flist = sys.argv[3:]
        getDataSum(tp, flist)
    else:
        usage()
        sys.exit()
	

if __name__ == "__main__":
    main()