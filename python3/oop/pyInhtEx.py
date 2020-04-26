# Author  : freeman
# Date    : 2020.04.26
# Version : 0.0.1
# Desc    :
#         : python OO programming -- super simple inheritance example
###################################################################

import os
import sys
import time

class Mammal(object):

    # Global Variables

    # default Constructor w/obj data members
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def __str__(self):
        return "Your name is: " + str(self.name)


class Cow(Mammal):

    # Global Variables

    # default Constructor
    def __init__(self, name, age, breed):
        Mammal.__init__(self, name)
        self.breed = breed
        self.age = age
        self.food = "grass"
        self.lang = "moo"
        self.hours = 5

    def getBreed(self):
        return self.breed

    def getAge(self):
        return self.age

    def speak(self):
        return self.lang

    def sleep(self):
        return self.hours

    def eat(self):
        return self.food

    def __str__(self):
        return str(self.breed) + " " + str(self.age)


def main():
    adam = Cow("angus", 3, "black")
    print(type(adam))
    print("Adam can speak: ", adam.speak(), " often times.")
    print("Adam will sleep: " , str(adam.sleep()), " hours per day.")
    print("Adam will eat: ", adam.eat()," most of the time.")
    print("Adam is a ", adam.__str__().split()[0], " Cow.")
    print("Adam has a name of: ", adam.getName())
    adam.setName("Frodo")
    print("Adam has a name of: ", adam.getName())


if __name__ == "__main__":
    main()
