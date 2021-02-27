class ListQueueError (Exception):
   pass

class ListQueue:
   
   def __init__ (self, maxSize=10):
      self.__queue = [None] * maxSize
      self.__maxSize = maxSize
      self.__numOfItems = 0
      
   
   def enqueue (self, itemToQueue):
      if not self.isFull():
         self.__queue[self.__numOfItems] = itemToQueue
         self.__numOfItems += 1
      else:   
         raise ListQueueError ("Unable to enqueue " + itemToQueue + " to a full ListQueue")         

      
   def dequeue (self):
      if not self.isEmpty():
         itemToReturn = self.__queue[0]
         for index in range (1, self.__numOfItems):
            self.__queue[index - 1] = self.__queue[index]
         #for index in range (0, self.__numOfItems - 1): #this loop is functionally identical to the previous loop
         #   self.__queue[index] = self.__queue[index + 1]
         self.__numOfItems -= 1
         return itemToReturn
      else:   
         raise ListQueueError ("Unable to dequeue from an empty ListQueue")         
   
   def isFull (self): #is there room to add any more information?
      return self.__numOfItems == self.__maxSize
   
   def isEmpty(self):
      return self.__numOfItems == 0
      
   def maxSize (self): #returns the size of the list - the maximum number of items that can be in the list
      return maxSize # or return len(self.__data)

   def __str__ (self):
      strToReturn = "Queue: "
      for index in range (self.__numOfItems):
         strToReturn += str(self.__queue[index]) + " " 
      return strToReturn   
      