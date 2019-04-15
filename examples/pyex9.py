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
        return "Animal is ready."

    def whoisthis(self, animal):
        return animal

    def swim(self, name, swim):
        if int(swim) == 0:
            return "This animal " + name + " can not swim like a boss"
        else:
            return "This animal " + name + " can swim like a boss"

class Dog(Mammal):

    # private variables
    breed = "Golden Retriever"

    def __init__(self, name, age, breed):
        super(Mammal, self).__init__()
        # If Dog class has data needed to be passed to parent class, one must do the following
        # Mammal.__init__(self, ParentVariables)
        self.name = name
        self.age = age
        self.breed = breed

    def setBreed(self,breed):
        self.breed = breed

    def getBreed(self):
        return self.breed

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def speak(self, lang):
        return "{} speaks {}".format(self.name, lang)

    def run(self):
        return "{} runs like a speedy hound".format(self.name)


class Cat(Mammal):

    breed = "Feline"

    def __init__(self, name, age, breed):
        super(Mammal, self).__init__()
        # if cat class has data needed to be passed to parent class, one must do the following
        # Mammal.__init__self(self, ParentVariables)
        self.name = name
        self.age = age
        self.breed = breed

    def setBreed(self, breed):
        self.breed = breed

    def getBreed(self):
        return self.breed

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


def main():
    amos = Dog("amos", 2, "Lab Retriever")
    bigbird = Cat("bigbird", 1, "Siamese")
    print amos.__class__.breed
    print amos.name
    print amos.age
    print amos.speak("woof")
    print amos.run()
    print "this is : " + amos.whoisthis(amos.getName())
    print amos.swim("amos", True)
    #amos.__class__.breed = "chiwawa"
    #print amos.__class__.breed
    print bigbird.swim("bigbird", False)

if __name__ == "__main__":
    main()
