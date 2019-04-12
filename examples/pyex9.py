# Author  : freeman
# Date    : 2019.04.11
# Version : 0.0.2
# Desc    : Program 9
#         : python OO programming -- simple inheritance example
###################################################################

import os
import sys
import time

class Mammal(object):

    # Global Variables

    # default Constructor
    def __init__(self):
        return "Dog is ready"

    def whoisthis(self):
        return "dog"

    def swim(self):
        return "dog can swim"

class Dog(Mammal):

    # private variables
    breed = "Golden Retriever"

    def __init__(self, name, age):
        super(Mammal, self).__init__()
        # If Dog class has data needed to be passed to parent class, one must do the following
        # Mammal.__init__(self, )
        self.name = name
        self.age = age

    def setBreed(self,breed):
        self.breed = breed

    def getBreed(self):
        return self.breed

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
    print "this is : " + amos.whoisthis()
    print "" + amos.swim()
    amos.__class__.breed = "chiwawa"
    print amos.__class__.breed

if __name__ == "__main__":
    main()
