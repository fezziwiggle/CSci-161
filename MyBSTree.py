'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 10a
ID#: 1325352

This program creates a class MyBSTree and adds 5 new functions to the original program.
The class allows the user to enter items and insert them into a tree.
The program then allows the user to find the minimum value, the maximum value,
the number of leaves, the height, and whether or not the tree is complete.

''' 

class BSTreeException(Exception):
   
   pass

class MyBSTree:
   
   class __TreeNode:
      
      def __init__ (self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right
      
   def __init__ (self):
      self.__numOfItems = 0
      self.__root = None
      #------------------------------
      #        MY CODE HERE
      #------------------------------
      self.__leafCount = 0
      self.__heightCount = 0
      self.__isComplete = True
      
   def insert (self, itemToInsert):
      if self.__root == None:
         self.__root = MyBSTree.__TreeNode(itemToInsert)
      else:
         location = self.__root
         done = False
         while not done:  #or while True
            if itemToInsert > location.data: #going to the right subtree
               if location.right == None: #nothing here right now, so this is where itemToInsert goes
                  location.right = MyBSTree.__TreeNode(itemToInsert)
                  done = True #end the loop   #break if using the infinite loop option in the while statement 
               else:
                  location = location.right
            else: #going to the left subtree     
               if location.left == None: #nothing here right now, so this is where itemToInsert goes
                  location.left = MyBSTree.__TreeNode(itemToInsert)
                  done = True #end the loop 
               else:
                  location = location.left
        
      self.__numOfItems += 1
   
   #def isEmpty(self):
      #return self.__numOfItems == 0
   
   def size(self):
      return self.__numOfItems
   
   def isInList (self, itemToFind):
      location = self.__root
      while location != None:
         if itemToFind == location.data:  #found it
            return True 
         elif itemToFind < location.data: 
            location = location.left
         else:   
            location = location.right
   
      return False
   
      
   def  __recIsInTree (self, itemToFind, location):
      if location == None: #one of the base cases
         return False
      elif location.data == itemToFind: #the other base case
         return True 
      elif itemToFind < location.data: #didn't find it yet, going left
         return self.__recIsInTree (itemToFind, location.left)
      else:
         return self.__recIsInTree (itemToFind, location.right)
      
      
   def recIsInList (self, itemToFind):
      return self.__recIsInTree (itemToFind, self.__root)
   
   #returns True if itemToInsert was not previously in the list - True indicates if was actually added to the list
   #returns False if itemToInsert was previously in the list and was not added again
   #either way itemToInsert will be in the list following this function 
   def recInsert (self, itemToInsert):
      if self.__root == None: #special case of inserting the first item
         self.__numOfItems += 1
         self.__root = self.__TreeNode (itemToInsert)
         return True 
      else:
         return self.__recInsert (itemToInsert, self.__root) #start our recursive function with the root
         
   def __recInsert (self, itemToInsert, location): #we know we have a node 
      if itemToInsert == location.data: #itemToInsert is already in the list
         return False
      elif itemToInsert < location.data:
         if location.left == None:
            self.__numOfItems += 1
            location.left = MyBSTree.__TreeNode(itemToInsert)
            return True
         else:
            return self.__recInsert (itemToInsert, location.left)                          
      else: #itemToInsert > location.data   
         if location.right == None:
            self.__numOfItems += 1
            location.right = MyBSTree.__TreeNode(itemToInsert)
            return True
         else:
            return self.__recInsert (itemToInsert, location.right)                          
         
   #assuming that the item to be inserted is not already in the list
   def recUniqueInsert (self, itemToInsert): 
      self.__numOfItems += 1
      if self.__root == None: #special case of inserting the first item
         self.__root = self.__TreeNode (itemToInsert)
      else:
         self.__recUniqueInsert (itemToInsert, self.__root) #start our recursive function with the root
         
   def __recUniqueInsert (self, itemToInsert, location): #we know we have a node 
      if itemToInsert < location.data:
         if location.left == None:
            location.left = MyBSTree.__TreeNode(itemToInsert)
         else:
            self.__recUniqueInsert (itemToInsert, location.left)                          
      else: #itemToInsert > location.data   
         if location.right == None:
            location.right = MyBSTree.__TreeNode(itemToInsert)
         else:
            self.__recUniqueInsert (itemToInsert, location.right)                          
      
   def __inOrder (self, location):
      if location != None: #do we have a node?
         self.__inOrder (location.left)
         print (location.data, end=' ')
         self.__inOrder (location.right)
         
      
   def inOrder (self):
      self.__inOrder (self.__root)
      
      
   def __postOrder (self, location):
      if location != None: #do we have a node?
         self.__postOrder (location.left)
         self.__postOrder (location.right)
         print (location.data, end=' ')
      
      
   def postOrder (self):
      self.__postOrder (self.__root)      
      
   
   #------------------------------
   #     BEGIN MY CODE HERE
   #------------------------------
   
   
   def isEmpty(self):
      if self.__root == None:
         return True
      else:
         return False
      
      
   def min(self): #returns the smallest value from the tree (the left-most item)
      if not self.isEmpty():
         if self.__root.left != None:
            location = self.__root.left
            while location != None:
               minValue = location.data
               location = location.left
         else:
            minValue = self.__root.data
         return minValue
      else:
         raise BSTreeException('Empty Tree Error')
      
      
   def max(self): #returns the largest value from the tree (the right-most item)
      if not self.isEmpty():
         if self.__root.right != None:
            location = self.__root.right
            while location != None:
               maxValue = location.data
               location = location.right
         else:
            maxValue = self.__root.data
         return maxValue
      else:
         raise BSTreeException('Empty Tree Error')
      

   def __numOfLeaves(self, location):
      if location.left == None and location.right == None:
         self.__leafCount += 1  
      else:
         if location.left != None:
            self.__numOfLeaves(location.left)
         if location.right != None:
            self.__numOfLeaves(location.right)
      return self.__leafCount
         

   def numOfLeaves(self):
      if not self.isEmpty():
         return self.__numOfLeaves(self.__root)
      else:
         return 0       
         
   
   def __height(self, location, currentHeight):

      if self.__root.left != None and self.__root.right != None:

         if location.left == None and location.right == None:
            pass

         else:
            
            if location.left != None:
               #currentHeight += 1                           
               #self.__height(location.left, currentHeight)
               #currentHeight -= 1      
               self.__height(location.left, currentHeight + 1)

            if location.right != None:
               #currentHeight += 1                           
               #self.__height(location.right, currentHeight)
               #currentHeight -= 1   
               self.__height(location.right, currentHeight + 1)
               
         if currentHeight > self.__heightCount:
            self.__heightCount = currentHeight

         return self.__heightCount

      else:
         self.__heightCount = 0
         return self.__heightCount         
   

   def height(self):
      if not self.isEmpty():
         self.__heightCount = 0 #this "resets" height count in case the function gets called a
         return self.__height(self.__root, 0) 
      else:
         return 0   
      
      
   def __complete(self, location): # CHECK FOR SPECIAL CASE IF THERE IS ONLY A ROOT
      
      #isComplete = True
      
      if location.left != None and location.right != None:
         self.__complete(location.left)
         self.__complete(location.right)
         
      elif location.left == None and location.right == None:
         pass #just an excuse to have this test
         
      else:
         self.__isComplete = False
         
      return self.__isComplete
         
      
      #if location.left != None:
         #self.__numOfLeaves(location.left)
         
      #if location.right != None:
         #self.__numOfLeaves(location.right)      
      
      
   def complete(self):
      if not self.isEmpty():
         self.__isComplete = True #this "resets" self.__isComplete from any prior calls to this function
         return self.__complete(self.__root)
      else:
         return False        
      
      