'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 9
ID#: 1325352

This program creates a class Deque that combines the functionality of a queue and a list. 
Items can be added/removed/peeked from only the front or back of the list.

'''

class DequeException(Exception):
    pass

class Deque:
    
    class __DequeNode:
        
        def __init__(self, item):
            self.item = item
            self.next = None
    
    def __init__(self):
        self.__numOfItems = 0
        self.__currentItem = None #currentItem starts at the first node
        self.__nextLocation = 0 #used to track which item to return in our __next__ function
    
        self.__head = None #will know where the first item in the list is at
        self.__tail = None #will know where the last item in the list is at
        self.__iterationNode = None      
    
    
    def __iter__ (self):
        self.__iterationNode = self.__head 
        return self #tells the built in for loop that the __next__ function will be in this object


    def __next__(self):
        if self.__iterationNode == None:
            self.__iterationNode = self.__head #set the variable up to start at the beginning the next time the for loop is used 
            raise StopIteration
        itemToReturn = self.__iterationNode.value
        self.__iterationNode = self.__iterationNode.next 
        return itemToReturn   
    
    
    def addFront(self, itemToAdd): #adds itemToAdd to beginning of the deque
        newNode = Deque.__DequeNode(itemToAdd)        
        if self.isEmpty(): #if the deque is empty, the head and tail are the new node
            self.__head = newNode
            self.__tail = newNode
        else: #if the deque is not empty, set itemToAdd to be new head
            oldHead = self.__head #save the node that was the old head
            self.__head = newNode #set new node to new head
            self.__head.next = oldHead #make the old head come directly after the new head 
        self.__numOfItems += 1
        return True
        
        
    def peekFront(self): #returns a copy of the first item in the deque, raises exception if called on empty deque
        if not self.isEmpty():
            return self.__head.item
        else:
            raise DequeException('Cannot peek from an empty deque')
        
        
    def removeFront(self): #removes first item from the deque, raises exception if called on empty deque
        if not self.isEmpty():
                    #prevLoc = self.__head
            location = self.__head.next
                    #if location != None:
                    #prevLoc.next = location.next
            self.__head = location
            while location != None:
                location = location.next
            self.__tail = location 
            self.__numOfItems -= 1
                
            return True
        else:
            raise DequeException('Cannot remove item from an empty deque')
        
        
    def addBack(self, itemToAdd): #adds itemToAdd to the end of the deque
        newNode = Deque.__DequeNode(itemToAdd)        
        if self.isEmpty(): #if the deque is empty, the head and tail are the new node
            self.__head = newNode
            self.__tail = newNode
        else: #if the deque is not empty, set itemToAdd to be new tail
            oldTail = self.__tail #save the node that was the old tail
            self.__tail = newNode #set new node to new tail
            oldTail.next = self.__tail #make the old head come directly before the new tail  
        self.__numOfItems += 1        
        return True
        
        
    def peekBack(self): #returns copy of the last item in the deque, raised exception if called on empty deque
        if not self.isEmpty():
            return self.__tail.item
        else:
            raise DequeException('Cannot peek from an empty deque')
        
        
    def removeBack(self): #removes the last item in the deque, raises exception if called on empty deque
        if not self.isEmpty():
            prevLoc = self.__head
            location = self.__head.next
            
            if location != None: #only enter this block if there is more than one item in the deque
                nextLoc = location.next
                
                while nextLoc != None:
                    prevLoc = prevLoc.next
                    location = location.next #this is the item to remove
                    nextLoc = nextLoc.next
                prevLoc.next = location.next
                
            
            else: #there is only one item in the deque
                prevLoc = location 
                self.__head = None
            
            
            self.__tail = prevLoc
            self.__numOfItems -= 1            
            return True
            
        else:
            raise DequeException('Cannot remove item from an empty deque')
        
    
    def size(self):
        return self.__numOfItems
        
        
    def isEmpty(self):
        return self.__numOfItems == 0
        
        
    def isInDeque(self, itemToFind): #returns true if itemToFind is in the deque, else returns false
        if not self.isEmpty():
            if itemToFind == self.__head.item:
                return True
            else:
                location = self.__head.next
                while location != None:
                    if location.item == itemToFind:
                        return True
                    location = location.next
                return False
        else:
            return False
        
        
    def removeItem(self, itemToRemove): #returns true if itemToRemove exists and is removed, else returns false
        if not self.isEmpty():
            if self.isInDeque(itemToRemove):
                if itemToRemove == self.__head.item:
                    prevLoc = self.__head
                    location = self.__head.next
                    self.__head = location
                    prevLoc.next = location.next
                else:
                    prevLoc = self.__head
                    location = self.__head.next
                    while location != None:
                        if location.item == itemToRemove:
                            prevLoc.next = location.next
                            return True
                        prevLoc = prevLoc.next
                        location = location.next
                    return False
                
            else:
                return False
        else:
            return False
        
        
    