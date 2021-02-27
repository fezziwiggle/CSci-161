'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 2
ID#: 1325352

This program creates a class called HonorPoints with instance variables
name, totalCredits, honorPoints, and totalPassedCredits for every new object created. 
The program then uses these variables in various methods to determine a GPA, compare GPAs,
and determine if a student can graduate. 


'''

class HonorPoints:
    
    REQUIRED_CREDITS = 20
    N0_GPA = -1
    
    def __init__(self, name = ''):
        
        self.__name = name
        self.setName(name)
        
        self.__totalCredits = 0
        self.__honorPoints = 0
        self.__totalPassedCredits = 0
        
    
    #setter methods ------------------------------
    
    def addClass(self, numCredits, grade): #the first argument is the number of credits, the second argument is the grade for the class.
        
        self.__totalCredits += numCredits #calculates total number of credits
        
        if grade == 'a' or grade == 'A': #lines 33-43 calculate honor points
            self.__honorPoints += (numCredits * 4)
        
        elif grade == 'b' or grade == 'B':
            self.__honorPoints += (numCredits * 3)
            
        elif grade == 'c' or grade == 'C':
            self.__honorPoints += (numCredits * 2)
        
        elif grade == 'd' or grade == 'D':
            self.__honorPoints += (numCredits * 1)
            
        if grade != 'f' or grade != 'F': #calculates total credits passed
            self.__totalPassedCredits += numCredits
            

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
    
    def getGPA(self): #retun NO_GPA if unable to calculate GPA
        
        if self.__totalCredits > 0:
            GPA = self.__honorPoints / self.__totalCredits
            
            return GPA
            
        else:
            return HonorPoints.N0_GPA
    
    def isSmarter(self, HonorPoints):
        
        if self.getGPA() > HonorPoints.getGPA():
            return True
        
        else:
            return False
        
    def canGraduate(self):
        
        if self.__totalPassedCredits >= HonorPoints.REQUIRED_CREDITS:
            return True
        
        else:
            return False