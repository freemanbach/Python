class Car:  # CLASS
    def __init__(self):
        self.carprice = 0
        self.carbrand = ""
        self.carmpg   = 0
        self.carspeed = 0
        self.horsepower = 0
        self.tires    = ""
        self.bodytype = ""
        
    def getCarSpeed(self): # Function / Method
        print "Car Speed is: {}".format(self.carspeed)
        
    def setCarSpeed(self, speed):
        self.carspeed = speed
    
    def getCarBrand(self): # Function / Method
        print "Car Brand is: {}".format(self.carbrand)

    def setCarBrand(self, brand): # Function / Method
        self.carbrand = brand

        
    def getCarPrice(self): # Function / Method
        print "Car Price is: {}".format(self.carprice)

    def setCarPrice(self, price): # Function / Method
        self.carprice = price
        
def main():
    lotus = Car() # Class
    #just b/c i cant spell farrarie
    print "Lotus: "
    lotus.setCarBrand("lotus")
    lotus.getCarBrand()
    lotus.setCarPrice(159999)
    lotus.getCarPrice() 
    # decreased in cost due to special reason
    lotus.setCarPrice(100000)
    lotus.getCarPrice() 
    lotus.setCarSpeed(240)
    lotus.getCarSpeed()
    
    print "Porsche: "
    porsche = Car()
    porsche.setCarBrand("Porsche")
    porsche.setCarPrice(169999)
    porsche.setCarSpeed(245)
    porsche.getCarBrand()
    porsche.getCarPrice()
    porsche.getCarSpeed()
    
main()
        
    
    