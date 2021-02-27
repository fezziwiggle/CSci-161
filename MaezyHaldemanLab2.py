'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 2
ID#: 1325352




'''

class HonorPoints:
    
    REQUIRED_CREDITS = 20
    NO_GPA = -1
    
    def __init__(self, name):
        
        self.__name = name
        self.setName(name)
        
        self.__totalCredits = 0
        self.__honorPoints = 0
        self.__totalPassedCredits = 0
        
    
    #setter methods ------------------------------
    
    def addClass(self, numCredits, grade): #the first argument is the number of credits, the second argument is the grade for the class.
        
        self.__totalCredits += numCredits #wrong logic, needs multiplication NOT addition, fix this
        
        if grade == 'a' or grade == 'A': 
            self.__honorPoints += 4
        
        elif grade == 'b' or grade == 'B':
            self.__honorPoints += 3
            
        elif grade == 'c' or grade == 'C':
            self.__honorPoints += 2
        
        elif grade == 'd' or grade == 'D':
            self.__honorPoints += 1
            

    def setName(self, name): #first last format
        
        self.__name = name
    
    #getter methods ------------------------------
    
    def getName(self): #returns the name of the student.
        
        return self.__name
    
    def getCredits(self): #returns the total number of credits taken so far.
        
        return self.__totalCredits
    
    def getPassedCredits(self): 
        
        return self.__totalPassedCredits
    
    def getHonorPoints(self): #returns the number of honor points earned so far.   
        
        return self.__honorPoints
    
    #other methods -------------------------------
    
    
