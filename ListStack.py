class ListStackError (Exception):
   pass

class ListStack:
   
   def __init__ (self, maxSize=10):
      self.__stack = [None] * maxSize
      self.__maxSize = maxSize
      self.__numOfItems = 0
      
   def push (self, itemToPush):      #adds an item to the top of the stack 
      if not self.isFull():
         self.__stack[self.__numOfItems] = itemToPush
         self.__numOfItems += 1
      else:   
         #raise Exception ("Unable to add " + itemToAdd + " to a full UnsortedList")
         raise ListStackError ("Unable to push " + itemToPush + " to a full ListStack")         

   def peek(self):  #returns the top item
      if not self.isEmpty():
         return self.__stack[self.__numOfItems - 1]
      else:   
         raise ListStackError ("Unable to peek from the ListStack")         
      
   def top(self): #removes the top item
      if not self.isEmpty():
         self.__numOfItems -= 1
      else:   
         raise ListStackError ("Unable to top from the ListStack")         

   def pop(self): #traditional way of accessing the stack - remove and return the "top" item    
      if not self.isEmpty():
         itemToReturn = self.__stack[self.__numOfItems - 1]
         self.__numOfItems -= 1
         return itemToReturn
      else:   
         raise ListStackError ("Unable to pop from the ListStack")         
      
      
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
