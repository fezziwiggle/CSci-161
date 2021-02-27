'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 3a
ID#: 1325352

This program creates a class that converts a user defined range into a noraml list range,
stores string data in the list, and creates methods that return indeces and strings from the list.

'''

class FlexibleArray:
    
    def __init__(self, lowIndex, highIndex, defaultValue = None):
        
        self.__maxSize = (highIndex - lowIndex) #the total number of AVAILABLE indexes we want in the list using the user range
        self.__ourList = [defaultValue] * self.__maxSize #creating a list with the maxSize number of indexes, every value in the list being 'None'
        self.__highIndex = highIndex
        self.__lowIndex = lowIndex
        
        
    
    def get(self, userIndex): # return the value at the specified index
        
        if self.__lowIndex <= userIndex <= self.__highIndex:
            
            ourIndex = (userIndex - self.__lowIndex)
            
            return self.__ourList[ourIndex]
        
        else:
            
            raise Exception('Index ' + str(userIndex) + ' out of range')
        
    
    def set(self, userIndex, value): #assigns a value to the specified index
        
        if self.__lowIndex <= userIndex <= self.__highIndex:
            
            ourIndex = (userIndex - self.__lowIndex) #turns the user index (range 1980 to 2020) into our index (range 0 to 40)
            self.__ourList[ourIndex] = value #assigns the user value to our index
           
            return True
        
        else:
            
            raise Exception('Index ' + str(userIndex) + ' out of range')
        
        
    def lowIndex(self):
        
        return self.__lowIndex
    
    
    def highIndex(self):
        
        return self.__highIndex
    
    
    def isInList(self, itemToFind): #returns True if itemToFind is in ourList, otherwise returns False
        
        if itemToFind in self.__ourList:
            
            return True
        
        else:
            
            return False
        
        
    def indexOf(self, itemToFind): #itemToFind = 'Maezy'
        
        if itemToFind in self.__ourList: #needs to take 'Maezy' and return 2002
            
            ourIndex = self.__ourList.index(itemToFind) #ourIndex will be 22, need to turn it into 2002
            indexToReturn = (self.__lowIndex + ourIndex)
            
            return indexToReturn
        
        else:
            
            raise Exception('Item ' + itemToFind + ' not in list')
        
            
        
        
        
        
        
        