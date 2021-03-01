"""
Author  : flo
date    : 2021.02.28
Purpose :
        :
Comments: need to implement additional functionalities before this is truly effective
        : May include Adler and CRC32 algorithm later
example : python hash.py -v
example : python hash.py -h
example : python hash.py -t shake_128 -g filename.zip
example : python hash.py -t blake2s -g filename.zip
example : python hash.py -t sha1 -g filename.zip
"""

import os
import sys
import hashlib  # main hashing libs 
import hmac     # message algorithm
import zlib     # adler and crc32

try:
    import whirlpool
except ImportError as err:
    print("Missing whirlpool Library !")
    sys.exit(1)    

try:
    import getopt   # parameter package lib
except ImportError as err:
    print("Missing GetOpt2 Library !")
    sys.exit(1)


__VERSION__ = "0.0.4"
__CURRENT_ALGORITHMS__ = ['md5', 'whirlpool', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224','sha3_256', 'sha3_384','sha3_512', 'shake_128', 'shake_256', 'blake2b','blake2s']
# shake_128 and shake_256 Digest Size
__DIGEST_SIZE__ = 32


def md5(fname):
    # https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
    # reading in 4k block at a time should be sufficient, others will use 1024 or 2048
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

def sha224(fname):
    hash_sha224 = hashlib.sha224()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha224.update(chunk)
    return hash_sha224.hexdigest()

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def sha384(fname):
    hash_sha384 = hashlib.sha384()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha384.update(chunk)
    return hash_sha384.hexdigest()

def sha512(fname):
    hash_sha512 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
    return hash_sha512.hexdigest()

def sha3_224(fname):
    hash_sha3_224 = hashlib.sha3_224()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_224.update(chunk)
    return hash_sha3_224.hexdigest()

def sha3_256(fname):
    hash_sha3_256 = hashlib.sha3_256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_256.update(chunk)
    return hash_sha3_256.hexdigest()

def sha3_384(fname):
    hash_sha3_384 = hashlib.sha3_384()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_384.update(chunk)
    return hash_sha3_384.hexdigest()

def sha3_512(fname):
    hash_sha3_512 = hashlib.sha3_512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha3_512.update(chunk)
    return hash_sha3_512.hexdigest()

def shake_128(fname):
    hash_shake_128 = hashlib.shake_128()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_shake_128.update(chunk)
    return hash_shake_128.hexdigest(__DIGEST_SIZE__)

def shake_256(fname):
    hash_shake_256 = hashlib.shake_256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_shake_256.update(chunk)
    return hash_shake_256.hexdigest(__DIGEST_SIZE__)

def blake2b(fname):
    hash_blake2b = hashlib.blake2b()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_blake2b.update(chunk)
    return hash_blake2b.hexdigest()

def blake2s(fname):
    hash_blake2s = hashlib.blake2s()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_blake2s.update(chunk)
    return hash_blake2s.hexdigest()

def whirlpool_hash(fname):
    hash_whirlpool = whirlpool.new()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_whirlpool.update(chunk)
    return hash_whirlpool.hexdigest()


def version():
    print(__VERSION__)


def chksumtypes():
    print("\nAvailable Algorithms: ")
    print("\t\t\t", str(__CURRENT_ALGORITHMS__))
    # print("\t\t\t", str(hashlib.algorithms_available))
    # print("\t\t\t", str(hashlib.algorithms_guaranteed))


def getCheckSum(tp, fp):
    if tp == "md5":
        chksum = md5(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "whirlpool":
        chksum = whirlpool_hash(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "sha1":
        chksum = sha1(fp)
        print(str(chksum), "\t", "*", str(fp))
    elif tp == "sha224":
        chksum = sha224(fp)
        print(str(chksum), "\t", "*", str(fp))
    elif tp == "sha256":
        chksum = sha256(fp)
        print(str(chksum), "\t", "*", str(fp))
    elif tp == "sha384":
        chksum = sha384(fp)
        print(str(chksum), "\t", "*",  str(fp))
    elif tp == "sha512":
        chksum = sha512(fp)
        print(str(chksum), "\t", "*", str(fp))
    elif tp == "sha3_224":
        chksum = sha3_224(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "sha3_256":
        chksum = sha3_256(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "sha3_384":
        chksum = sha3_384(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "sha3_512":
        chksum = sha3_512(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "shake_128":
        chksum = shake_128(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "shake_256":
        chksum = shake_256(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "blake2s":
        chksum = blake2s(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    elif tp == "blake2b":
        chksum = blake2b(fp)
        print(str(chksum), "\t",  "*",  str(fp))
    else:
        print("There is no other option !")
        sys.exit(1)


def failed():
    print("File and Software checksum did not MATCHed !")
    print("Quiting.....................................")
    sys.exit(1)


def verifyCheckSum(tp, fp, cksumf):

    with open(cksumf, "r+") as f:
        a = f.read()
    cs = a.split()[0]

    if tp == "md5":
        chksum = md5(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha1":
        chksum = sha1(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ",  "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha224":
        chksum = sha224(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha256":
        chksum = sha256(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha384":
        chksum = sha384(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ",  "\t",  str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha512":
        chksum = sha512(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha3_224":
        chksum = sha3_224(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha3_256":
        chksum = sha3_256(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ",  "\t",  str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha3_384":
        chksum = sha3_384(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "sha3_512":
        chksum = sha3_512(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "shake_128":
        chksum = shake_128(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "shake_256":
        chksum = shake_256(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ",  "\t",  str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "blake2b":
        chksum = blake2b(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "blake2s":
        chksum = blake2s(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    elif tp == "whirlpool":
        chksum = whirlpool_hash(fp)
        if chksum == cs:
            print("The file\'s checksum and checksumming this file here MATCHed !")
            print("File checksum    : ", "\t", str(cs))
            print("software checksum: ", "\t", str(chksum))
        else:
            failed()
    else:
        print("There is no other option !")
        sys.exit(1)

def usage():

    # Help info
    usage = """
            usage: python hash.py [-t,--tp = checksum_algorithm] [-g,--gp = filename] 
                                  [-c,--cs = filename.{md5:sha1:sha224:sha256:sha384:sha512:sha3_224:sha3_256:sha3_384:sha3_512:shake_128: \
                                                                            blake2b:blake2s:whirlpool}]    [-h] [-v]

			
            examples:
            python hash.py
            python hash.py -t sha1 -g linux.iso 
            python hash.py -t sha1 -g linux.iso -c filename.{md5:sha1:sha224:sha256:sha384:sha512:sha3_224:sha3_256:sha3_384:sha3_512:shake_128: \
                                                                            blake2b:blake2s:whirlpool}

            python hash.py -v
            python hash.py -h

            options :
            -t, --tp=value, --tp value  Collision Algorithms {md5:sha1:sha224:sha256:sha384:sha512:sha3_224:sha3_256:sha3_384:sha3_512:shake_128: \
                                                                            blake2b:blake2s:whirlpool}

            -g, --gp=value, --gp value  file to check to get checksum
            -c, --cs=value, --cs value  supply this value, this software will verify the 
			                            checksum against the downloaded file
            -v                          show program's version number and exit
            -h                          show this help message and exit
            """

    print(usage)


# Let the main be here
def main():

    # default values
    typ, filename, csumf = "", "", ""

    # using getopt function for giggles
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:g:c:vh', ['tp=', 'gp=', 'cs='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # pull data from getopt
    for o, a in opts:
        if o in ('-t', '--tp'):
            if a.strip().lower() == "md5":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha1":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha224":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha256":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha384":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha512":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha3_224":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha3_256":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha3_384":
                typ = a.strip().lower()
            elif a.strip().lower() == "sha3_512":
                typ = a.strip().lower()
            elif a.strip().lower() == "shake_128":
                typ = a.strip().lower()
            elif a.strip().lower() == "shake_256":
                typ = a.strip().lower()
            elif a.strip().lower() == "blake2b":
                typ = a.strip().lower()
            elif a.strip().lower() == "blake2s":
                typ = a.strip().lower()
            elif a.strip().lower() == "whirlpool":
                typ = a.strip().lower()
            else:
                print("Please enter the limited correct type of file Collision Algorithm available to you. ")
                chksumtypes()
                sys.exit(2)
        elif o in ('-g', '--gp'):
            if os.path.isfile(a.strip().lower()):
                filename = a.strip().lower()
            else:
                print("Please enter in your source file. ")
                sys.exit(2)
        elif o in ('-c', '--cs'):
            if os.path.isfile(a.strip().lower()):
                csumf = a.strip().lower()
            else:
                print("Please enter in your checksum file.")
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


    # the brain of the operation
    if len(sys.argv) == 7:
        verifyCheckSum(typ,filename,csumf)
    elif len(sys.argv) == 5:
        getCheckSum(typ,filename)
    else:
        usage()
        sys.exit()
	

if __name__ == "__main__":
    main()
