'''
Maezy Haldeman: m.haldeman@und.edu
CS161: CompSci 2
Midterm Lab Exam
ID#: 1325352

'''

class Car:
    
    def __init__(self, model=None, year=None, mileage=None): #defaults to no info, can set values using setter methods
        
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        
        
    #setters
    
    def setModel (self, model):
        
        self.__model = model
        return True
        
    
    def setYear(self, year):
        
        if 1900 <= year <= 2019:
            self.__year = year
            return True
        else:
            return False
        
    
    def setMileage(self, mileage):
        
        if 0 <= mileage <= 1000000:
            self.__mileage = mileage
            return True
        else:
            return False
        
    
    #getters
    
    def getModel(self):
        
        return self.__model
        
    
    def getYear(self):
        
        return self.__year
        
    
    def getMileage(self):
        
        return self.__mileage
        
    
    #other methods
    
    def equals(self, car):
        
        if self.__model == car.__model and self.__year == car.__year and self.__mileage == car.__mileage:
            return True
        else:
            return False
        
    
    def highMileage(self):
        
        if self.__mileage >= 125000:
            return True
        else:
            return False
        
    
    def __str__(self):
        
        string = ('Model: ' + self.__model + '\n' + 'Year: ' + str(self.__year) + '\n' + 'Mileage: ' + str(self.__mileage))
        return string