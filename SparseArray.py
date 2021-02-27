'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 7a
ID#: 1325352

This program creates a class that allows the user to create and modify a "sparse array" 
using linked lists. The user can add, update, and remove nodes from the linked list
as well as choose the default value for "nonexistent" nodes.

'''

class SparseArrayException(Exception):
    pass

class SparseArray:
    
    class __ArrayNode:   
            
        def __init__(self, row, col, value):
             
            self.row = row
            self.col = col
            self.value = value
            self.next = None #self-referential - will store the location of another Node    
            
    
    def __init__(self, defaultValue, maxRowSize=1000, maxColSize=1000):
        
        self.__maxRowSize = maxRowSize
        self.__maxColSize = maxColSize
        self.__defaultValue = defaultValue
        
        self.__numOfItems = 0
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
    
        
    def getDefaultValue(self):
        return self.__defaultValue
        
    
    def get(self, row, col):
        
        if row <= self.__maxRowSize and col <= self.__maxColSize:
            if self.__head.row == row and self.__head.col == col: #is the node to get the first node?
                return self.__head.value      
            else: #the node to get is not the first node, start looking through the linked list
                location = self.__head.next
                while location != None:
                    if location.row == row and location.col == col:
                        return location.value #if we found a matching node, return the node at those coordinates
                    location = location.next
                return self.__defaultValue #if we went through the list and did not find a matching node, return the default value
                    
        else:
            raise SparseArrayException('Invalid row/col for range')            

          
    def set(self, row, col, value): #dont compare numbers to values. compare values to values
        
        if value != self.__defaultValue: #we are setting an actual value
            if row <= self.__maxRowSize and col <= self.__maxColSize: 
                newNode = SparseArray.__ArrayNode(row, col, value) #set/update new node
                
                if self.__head == None: #if the linked list is empty, set first item to our node
                    self.__head = newNode
                    self.__tail = newNode
                    self.__numOfItems += 1  
                    
                elif self.__head.row == row and self.__head.col == col: #if the list is not empty and row/col are valid, check if the first item matches
                    self.__head = newNode
                    
                else: #first item does not match, start looking through the rest of the linked list to see if any other nodes match
                    location = self.__head.next
                    
                    while location != None: #is there more than one item in the list?
                        if location.row == row and location.col == col: #we've found a matching node, so update it
                            #THIS LINE
                            location.value = newNode.value
                            #THIS LINE
                            break
                        location = location.next                          
                            
                    if location == None: #we've reached the end of the list without finding a matching node, so make a new one
                        self.__tail.next = newNode
                        self.__numOfItems += 1
                        self.__tail = newNode

            else:
                raise SparseArrayException('Invalid row/col for range')
        
        else: #if value IS defaultValue
            
            if self.__head.row == row and self.__head.col == col: #if the first node matches, update 
                self.__head = self.__head.next
                if self.__tail.value == value:
                    self.__tail = None
                return True
            else: #first node doesn't match, so start going through the list to see if any other nodes match
                location = self.__head.next
                prevLoc = self.__head
                while location != None:
                    if location.row == row and location.col == col:
                        if location.next == None:
                            self.__tail = prevLoc
                        prevLoc.next = location.next
                        return True
                    else:
                        prevLoc = location
                        location = location.next                
                        
                raise SparseArrayException('Invalid row/col for range')
                       
        
        
        