# Author  : freeman
# Date    : 2019.04.08
# Version : 0.0.1
# Desc    : Program 9
#         : simple OO programming
###################################################################

import os
import sys
import time

class Mammal(object):
    def __init__(self):
        print "Dog is ready"

    def whoisthis(self):
        print "dog"

    def swim(self):
        print "dog can swim"

class Dog(Mammal):

    breed = "Golden Retriever"

    def __init__(self, name, age):
        super(Mammal, self).__init__()
        self.name = name
        self.age = age

    def speak(self, lang):
        return "{} speaks {}".format(self.name, lang)

    def run(self):
        return "{} runs like a speedy hound".format(self.name)

def main():
    amos = Dog("amos", 2)
    print amos.__class__.breed
    print amos.name
    print amos.age
    print amos.speak("woof")
    print amos.run()
    amos.whoisthis()
    amos.swim()

if __name__ == "__main__":
    main()
