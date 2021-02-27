from BSTree import BSTree

def main ():
   tree = BSTree()
   print ("Is tree empty - should be true: ", tree.isEmpty())
   print ("Number of nodes - should be 0: ", tree.size())
   tree.insert ("m")
   tree.insert ("b")
   tree.insert ("e")
   tree.insert ("d")
   tree.insert ("a")
   tree.insert ("s")
   tree.insert ("t")
   tree.insert ("o")
   tree.recUniqueInsert ("r")
   print ("Was g actually added? ", tree.recInsert ("g"))
   print ("Was g actually added? ", tree.recInsert ("g"))

   print ("Is tree empty - should be false: ", tree.isEmpty())
   print ("Number of nodes - should be 8: ", tree.size())
   
   #print ("Is m in the list? ", tree.isInList ("m"))
   #print ("Is a in the list? ", tree.isInList ("a"))
   #print ("Is q in the list? ", tree.isInList ("q"))
   
   print ("Is m in the list? ", tree.recIsInList ("m"))
   print ("Is a in the list? ", tree.recIsInList ("a"))
   print ("Is q in the list? ", tree.recIsInList ("q"))
   
   tree.inOrder()
   tree.postOrder()
   
main()   