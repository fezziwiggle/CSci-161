'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 5a
ID#: 1325352

This program creates a class PriorityQueue which allows the user to enqueue items with a 
priority number 1-100 (using inner class __Node),
queuing items wither higher priority numbers higher in the queue. 

'''

class PriorityQueueException (Exception):
    pass

class PriorityQueue:
    
    #-------------------------------------------------------------
    class __Node:                                                
        
        def __init__(self, item, priority):
            self.item = item
            self.priority = priority
            
        def setPriority(self, priority):
            self.priority = priority
    #-------------------------------------------------------------

    def __init__ (self, maxSize=100):
        self.__queue = [None] * maxSize #OUR LIST
        self.__maxSize = maxSize      
        self.__numOfItems = 0   
        

    def enqueue (self, itemToQueue, priority = 1):
        if not self.isFull() and 1 <= priority <= 100:
            indexForNewItem = self.__numOfItems
            
            for index in range(self.__numOfItems):
                if priority > self.__queue[index].priority: #find first item with smaller priority
                    indexForNewItem = index #remember that location
                    
                    for index2 in range (self.__numOfItems, index, -1): #SKETCH THIS OUT. WHY DOES THIS BLOCK OF CODE WORK???
                        self.__queue[index2] = self.__queue[index2 -1] #move following items to the right
                        
                    break
                        
            self.__numOfItems += 1
            self.__queue[indexForNewItem] = PriorityQueue.__Node(itemToQueue, priority) 
            
        elif self.isFull():   
            raise PriorityQueueException ("Unable to enqueue " + itemToQueue + " to a full queue")    
        else:
            raise PriorityQueueException ('Unable to enqueue ' + itemToQueue + ' with an out-of-range priority')        
    

    def dequeue (self):
        if not self.isEmpty():
            itemToReturn = self.__queue[0].item
            #for index in range (1, self.__numOfItems):
            #    self.__queue[index - 1] = self.__queue[index]
            for index in range (0, self.__numOfItems - 1): #this loop is functionally identical to the previous loop
                self.__queue[index] = self.__queue[index + 1]
            self.__numOfItems -= 1
            return itemToReturn
        else:   
            raise PriorityQueueException ("Unable to dequeue from an empty queue")   
        

    def isFull (self): #is there room to add any more information?
        return self.__numOfItems == self.__maxSize


    def isEmpty(self):
        return self.__numOfItems == 0


    def maxSize (self): #returns the size of the list - the maximum number of items that can be in the list
        return self.__maxSize # or return len(self.__data)


    def __str__ (self):
        strToReturn = "Queue: "
        for index in range (self.__numOfItems):
            strToReturn += str(self.__queue[index].item) + " " 
        return strToReturn   


