class BSTree:
   
   class __TreeNode:
      
      def __init__ (self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right
      
   def __init__ (self):
      self.__numOfItems = 0
      self.__root = None
      
   def insert (self, itemToInsert):
      if self.__root == None:
         self.__root = BSTree.__TreeNode(itemToInsert)
      else:
         location = self.__root
         done = False
         while not done:  #or while True
            if itemToInsert > location.data: #going to the right subtree
               if location.right == None: #nothing here right now, so this is where itemToInsert goes
                  location.right = BSTree.__TreeNode(itemToInsert)
                  done = True #end the loop   #break if using the infinite loop option in the while statement 
               else:
                  location = location.right
            else: #going to the left subtree     
               if location.left == None: #nothing here right now, so this is where itemToInsert goes
                  location.left = BSTree.__TreeNode(itemToInsert)
                  done = True #end the loop 
               else:
                  location = location.left
        
      self.__numOfItems += 1
   
   def isEmpty(self):
      return self.__numOfItems == 0
   
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
            location.left = BSTree.__TreeNode(itemToInsert)
            return True
         else:
            return self.__recInsert (itemToInsert, location.left)                          
      else: #itemToInsert > location.data   
         if location.right == None:
            self.__numOfItems += 1
            location.right = BSTree.__TreeNode(itemToInsert)
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
            location.left = BSTree.__TreeNode(itemToInsert)
         else:
            self.__recUniqueInsert (itemToInsert, location.left)                          
      else: #itemToInsert > location.data   
         if location.right == None:
            location.right = BSTree.__TreeNode(itemToInsert)
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