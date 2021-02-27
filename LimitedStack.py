'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 5b
ID#: 1325352

This program creates a class LimitedStack and allows the user to create a stack of their desired size (defaults to 10 if none given),
and allows the user to add and remove items from the stack. When the stack becomes full, the item at the bottom of the stack is deleted and 
the new item is added to the top of the stack.

'''

class LimitedStackError (Exception):
    pass

class LimitedStack:

    def __init__ (self, maxSize=10):
        self.__stack = [None] * maxSize
        self.__maxSize = maxSize
        self.__numOfItems = 0
        

    def push (self, itemToPush):      #adds an item to the top of the stack 
        if not self.isFull():
            self.__stack[self.__numOfItems] = itemToPush
            self.__numOfItems += 1
            
        elif self.isFull():
            indexForNewItem = (self.__maxSize -1)
            
            for index in range (0, self.__numOfItems - 1):
                self.__stack[index] = self.__stack[index + 1]
            self.__stack[indexForNewItem] = itemToPush
            

    def peek(self):  #returns the top item
        if not self.isEmpty():
            return self.__stack[self.__numOfItems - 1]
        else:   
            raise LimitedStackError ("Unable to peek from the LimitedStack")      
        

    def top(self): #removes the top item
        if not self.isEmpty():
            self.__numOfItems -= 1
        else:   
            raise LimitedStackError ("Unable to top from the LimitedStack")      
        

    def pop(self): #traditional way of accessing the stack - remove and return the "top" item    
        if not self.isEmpty():
            itemToReturn = self.__stack[self.__numOfItems - 1]
            self.__numOfItems -= 1
            return itemToReturn
        else:   
            raise LimitedStackError ("Unable to pop from the LimitedStack")    


    def isFull (self): #is there room to add any more information?
        return self.__numOfItems == self.__maxSize
    

    def isEmpty(self):
        return self.__numOfItems == 0
    

    def maxSize (self): #returns the size of the list - the maximum number of items that can be in the list
        return maxSize # or return len(self.__data)
    

    def __str__ (self):
        #for release I might do this
        #return "ListStack object - version 0.01, last updated 7/14/2020"
        strToReturn = "Data: "
        for index in range (self.__numOfItems):
            strToReturn += self.__stack[index] + " " 
        return strToReturn   
