#!/usr/bin/env python3
"""
Author        :
Date          : 20201020
version       : 0.0.1
desc          : morsecode translator from the abyss
"""

def task1():
    a = [1,3,5,7,9]
    b = [2,4,6,8,10]
    c = []
    for i in a:
        if i == 9:
            c.append(i*2)
        else:
            c.append(0)
    print("My answer is: ", c)

# bit, restclient, 
def recip(v):
    if (v != 0) or (v != 1):
        # do something
        sol, value = [], str(v)
        c, tmp2 = 2, sorted(value)
        for a in list(range(2, 11)): # can alter end value
            sol.append(str(a*v))
        for a in sol:
            tmp1 = sorted(a)
            if tmp1 == tmp2:
                print("Yes, match number at {}".format(c))
                c+=1
            else:
                print("No, Not match number at {}".format(c))
                c+=1
                

# ingridients
def con2mc(mess):
    ans = ""
    c2mc = { 'A':'.-', 'B':'-...', 
              'C':'-.-.' , 'D':'-..', 'E':'.', 
              'F':'..-.', 'G':'--.', 'H':'....', 
              'I':'..', 'J':'.---', 'K':'-.-', 
              'L':'.-..', 'M':'--', 'N':'-.', 
              'O':'---', 'P':'.--.', 'Q':'--.-', 
              'R':'.-.', 'S':'...', 'T':'-', 
              'U':'..-', 'V':'...-', 'W':'.--', 
              'X':'-..-', 'Y':'-.--', 'Z':'--..', 
              '1':'.----', '2':'..---', '3':'...--', 
              '4':'....-', '5':'.....', '6':'-....', 
              '7':'--...', '8':'---..', '9':'----.', 
              '0':'-----', ',':'--..--', '.':'.-.-.-', 
              '?':'..--..', '/':'-..-.', '-':'-....-', 
              '(':'-.--.', ')':'-.--.-', ' ':'|'}

    for i in mess:
        ans+=c2mc.get(i) + " "
    print("Your message is MorseCode is: ", ans)



def con2c(mess):
    tmp = mess.split(' ')
    ans = ""
    mc2c = {'.-': 'A', '-...': 'B', '-.-.': 'C',
            '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I',  
            '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', 
            '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', 
            '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', 
            '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', 
            '--...': '7', '---..': '8', '----.': '9',
            '--..--':',', '.-.-.-':'.', '..--..':'?',
            '-..-.':'/', '-....-':'-', '-.--.':'(',
            '-.--.-':')', '|':' ', ' ':''}
    for i in tmp:
        ans+=mc2c.get(i)
    print("Your MorseCode came to: ", ans)


def main():
    # Morse Code conveter tool
    ui = input("Enter in a phrase? ").strip()
    if ui.split(' ')[0].isalnum():
        con2mc(ui.upper())
    else:
        con2c(ui)


if __name__ == "__main__":
    main()
