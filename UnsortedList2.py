'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 3b
ID#: 1325352

This program takes the class UnsortedList and adds 4 new methods, replaceAll, removeAll, count, and partial match.

'''

class UnsortedList2:

    def __init__ (self, maxSize=10):
        self.__data = [None] * maxSize #create the entire list, with each item having the value None
        self.__maxSize = maxSize
        self.__numOfItems = 0
        self.__currentItem = 0 #index of which item should be returned when calling getNextItem()
        
        self.__itemToFind = None #M Y  C O D E  H E R E 

    def add (self, itemToAdd):      
        if not self.isFull():
            self.__data[self.__numOfItems] = itemToAdd
            self.__numOfItems += 1
        else:   
            raise Exception ("Unable to add " + itemToAdd + " to a full UnsortedList")

    def add2 (self, itemToAdd):      #original add, returns True if an item was added (there was room to add it), otherwise returns False
        if not self.isFull():
            self.__data[self.__numOfItems] = itemToAdd
            self.__numOfItems += 1
            return True
        else:   
            return False

    def __findIndexOf (self, itemToFind):
        for index in range (0, self.__numOfItems):
            if itemToFind == self.__data[index]:
                return index 
        return -1    

    def remove (self, itemToRemove):
        for index in range (0, self.__numOfItems):
            if itemToRemove == self.__data[index]:
                self.__data[index] = self.__data[self.__numOfItems - 1]
                self.__numOfItems -= 1
                return True

        return False   

    def remove3 (self, itemToRemove):  #copy of remove, but using findIndexOf 
        indexLoc = self.__findIndexOf (itemToRemove)
        if indexLoc >= 0:      
            self.__data[indexLoc] = self.__data[self.__numOfItems - 1]
            self.__numOfItems -= 1
            return True

        return False   

    def remove2 (self, itemToRemove):  #original remove
        for index in range (0, self.__numOfItems):
            if itemToRemove == self.__data[index]:
                for index2 in range (index, self.__numOfItems -1): 
                    self.__data[index2] = self.__data[index2 + 1]
                self.__numOfItems -= 1
                return True

        return False   

    def isInList (self, itemToFind):
        #if self.__findIndexOf (itemToFind) >= 0:
        #   return True
        #else:
        #   return False

        return self.__findIndexOf (itemToFind) >= 0

        #for index in range (0, self.__numOfItems):
        #   if itemToFind == self.__data[index]:
        #      return True
        #return False   

    def isFull (self): #is there room to add any more information?
        return self.__numOfItems == self.__maxSize

    def isEmpty(self):
        return self.__numOfItems == 0

    def maxSize (self): #returns the size of the list - the maximum number of items that can be in the list
        return maxSize # or return len(self.__data)

    def size (self): #returns the number of items in the list
        return self.__numOfItems

    def reset(self):
        self.__currentItem = 0

    def getNextItem(self):
        temp = self.__data[self.__currentItem]
        self.__currentItem += 1
        if self.__currentItem == self.__numOfItems: #have we gone past the end of our data
            self.__currentItem = 0 #go back to the beginning 

        return temp 
    
    
#================================================================================

#BEGIN MY CODE HERE

#================================================================================


    def removeAll(self, itemToRemove): #the only difference between this and remove() is that removeAll() returns numRemoved instead of True
        
        numRemoved = 0
        for index in range (0, self.__numOfItems):
            if itemToRemove == self.__data[index]:
               
                self.__data[index] = self.__data[self.__numOfItems - 1] 
                self.__numOfItems -= 1
                numRemoved += 1
                
        return numRemoved
                     
    
    def replaceAll(self, newValue, originalValue):
        
        numReplaced = 0
        for index in range (0, self.__numOfItems):
            if originalValue == self.__data[index]:
    
                self.__data[index] = newValue
                numReplaced += 1
    
        return numReplaced
    
        
    def count(self, valueToCount):
        occurences = 0
        for index in range (0, self.__numOfItems):
            if valueToCount == self.__data[index]:
                occurences += 1
        return occurences
    
        
    def partialMatch(self, itemToFind = None):
  
        if itemToFind == None and self.__currentItem == 0:
            raise Exception('None type unnacceptable for initial search criteria')
  
        elif itemToFind != None:
            self.__itemToFind = itemToFind
            for index in range (0, self.__numOfItems):
                if itemToFind in self.__data[index]:
                    self.__currentItem += 1                    
                    return self.__data[index]
    
        elif itemToFind == None:
            for index in range (self.__currentItem, self.__numOfItems):
                self.__currentItem += 1                
                if self.__itemToFind in self.__data[index]:
                    if self.__currentItem != index:
                        return self.__data[index]
                    
            




