'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 6b
ID#: 1325352

This program creates a class UnsortedCountList and allows the user to create a list and add/remove items
and return certain information about the list. Rather than allowing duplicate items to be added,
the program increments the itemCount of an item using an inner class.

'''

class UnsortedCountListAddError (Exception):
   pass

class UnsortedCountListGetNextItemError(Exception):
   pass

class UnsortedCountList:
   
   #-------------------------------------------------------------
   class __Node:                                                

      def __init__(self, item, itemCount=0): #when a duplicate item is added, make sure to increment self.itemCount somewhere in the main class
         self.item = item
         self.itemCount = itemCount

      def setCount(self, itemCount):
         self.itemCount = itemCount
   #-------------------------------------------------------------
   
   def __init__ (self, maxSize = 100):
      self.__data = [None] * maxSize #create the entire list, with each item having the value None
      self.__maxSize = maxSize
      self.__numOfItems = 0
      self.__currentItem = 0 #index of which item should be returned when calling getNextItem()
      self.__nextLocation = 0 #used to track which item to return in our __next__ function
      

   def __iter__ (self):
      return self
   
   
   def __next__ (self):
      if self.__nextLocation == self.__numOfItems: #have we gone past the end of the list?
         self.__nextLocation = 0 #set us up to start at the beginning next time the for loop is used with our object 
         raise StopIteration   
      temp = self.__data[self.__nextLocation]
      self.__nextLocation += 1
      return temp 

      
   def add (self, itemToAdd): #returns True if an item was added (there was room to add it), otherwise returns False
      if not self.isFull():
         itemOccurences=0
         
         if self.isEmpty():
            itemOccurences = 1
            self.__data[self.__numOfItems] = UnsortedCountList.__Node(itemToAdd, itemOccurences)  #if the list is empty, create a new item 
            self.__numOfItems += 1            
            
         else:
            for index in range (0, self.__numOfItems):
               if self.__data[index].item != itemToAdd:
                  itemOccurences = 1
                  self.__data[self.__numOfItems] = UnsortedCountList.__Node(itemToAdd, itemOccurences) #if the list is not empty but itemToAdd IS NOT in the list, create a new item
                  self.__numOfItems += 1                  
                  break
               
               elif self.__data[index].item == itemToAdd:
                  itemOccurences = self.__data[index].itemCount #changes itemOccurences to the itemCount of the existing item
                  itemOccurences += 1 #increments the the count of itemOccurences 
                  self.__data[index].itemCount = itemOccurences #if the list is not empty but itemToAdd IS in the list, update the count of that item
                  break
                           
         return True
         
      else:
         return False   
      
      
   def remove (self, itemToRemove):
      for index in range (0, self.__numOfItems):
         
         if self.__data[index].item == itemToRemove: 
            if self.__data[index].itemCount > 1: #if the itemCount is greater than 1
               self.__data[index].itemCount -= 1 #then decrement the itemCount
            else: #if itemCount is 1
               self.__data[index] = self.__data[self.__numOfItems - 1] #replace the location of the itemToRemove with the last item in the list
               self.__numOfItems -= 1 #decrement numOfItems to "delete" the now duplicate last item a
            return True  
         else:
            return False    
               
      
   def __findIndexOf (self, itemToFind):
      for index in range (0, self.__numOfItems):
         if self.__data[index].item == itemToFind:
            return index 
      return -1  
   
   
   def isInList (self, itemToFind):
      return self.__findIndexOf (itemToFind) >= 0
      

   def isFull (self): #is there room to add any more information?
      return self.__numOfItems == self.__maxSize
   
   
   def isEmpty(self):
      return self.__numOfItems == 0
   
      
   def maxSize (self): #returns the size of the list - the maximum number of items that can be in the list
      return maxSize # or return len(self.__data)
 
   
   def size (self): #returns the number of UNIQUE items in the list
      return self.__numOfItems
 
   
   def overallCount(self): #returns the total number of all items in the list (sum of all items' itemCount)
      overallCount = 0
      for index in range (0, self.__numOfItems):
         overallCount += self.__data[index].itemCount
      return overallCount
   
   
   def count(self, item): #returns the itemCount of a specific item in the list
      for index in range (0, self.__numOfItems):
         if self.__data[index].item == item:
            return self.__data[index].itemCount
      else:
         return 0
   
   
   def reset(self):
      self.__currentItem = 0
 
   
   def getNextItem(self):
      temp = self.__data[self.__currentItem].item
      self.__currentItem += 1
      if self.__currentItem == self.__numOfItems: #have we gone past the end of our data
         self.__currentItem = 0 #go back to the beginning         
      return temp 
   
   
             
      
      