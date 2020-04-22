
# abstraction
class Cat:


    def __init__(self, cname, cage, ccolor):
        # encapsulation
        self.cname = cname
        self.cage = cage
        self.ccolor = ccolor
        self.whiskers = 30
        self.paws = 4

    def getName(self):
        return self.cname

    def setName(self, name):
        self.cname = name

    def getAge(self):
        return self.cage

    def getColor(self):
        return self.ccolor

    def getPaws(self):
        return self.paws

    def setAge(self, age):
        self.cage = age

    def __str__(self):
        return str(self.cname) + " " + str(self.cage) + " " + str(self.paws)



def main():
    joan = Cat("joan", 7, "yellow")
    print(type(joan))
    print("the name of my cat is: ", joan.getName())
    print("the age of my cat is: ", joan.getAge())
    joan.setAge(29)
    print("New cat age afterall: ", joan.getAge())



if __name__ == "__main__":
    main()
