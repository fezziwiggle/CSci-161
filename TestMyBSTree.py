'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 10a
ID#: 1325352

This program tests the functionality of the class MyBSTree, mainly the functions
min, max, height, numOfLeaves, and complete.

'''

from MyBSTree import *

def main ():
    tree = MyBSTree()
    print ("Is tree empty - should be true: ", tree.isEmpty())
    print ("Number of nodes - should be 0: ", tree.size())
    print()
    
    tree.insert ("m")
    tree.insert ("b")
    tree.insert ("e")
    tree.insert ("d")
    tree.insert ("a")
    tree.insert ("s")
    tree.insert ("t")
    tree.insert ("o")
    tree.recUniqueInsert ("r")
    print()
    
    print ("Was g actually added? ", tree.recInsert ("g"))
    print ("Was g actually added? ", tree.recInsert ("g"))
    print()
    
    print ("Is tree empty - should be false: ", tree.isEmpty())
    print ("Number of nodes - should be 8: ", tree.size())
    print()
    
    #print ("Is m in the list? ", tree.isInList ("m"))
    #print ("Is a in the list? ", tree.isInList ("a"))
    #print ("Is q in the list? ", tree.isInList ("q"))
    
    print ("Is m in the list? ", tree.recIsInList ("m"))
    print ("Is a in the list? ", tree.recIsInList ("a"))
    print ("Is q in the list? ", tree.recIsInList ("q"))
    print()
    
    tree.inOrder()
    tree.postOrder()
    print()
    print()
    
    print('Minimum value:', tree.min())
    print('Maximum value:', tree.max())
    print()
    
    print('Number of leaves in the tree:', tree.numOfLeaves())
    print('Height of the tree:', tree.height())  #should return 3
    print('Is the tree complete?', tree.complete())
    print()
    
    print('Adding "n" to the tree...')
    tree.insert ("n")
    print()
    
    print('Is the tree complete?', tree.complete())
    print()    
    
    print('Adding "f" to the tree...')
    tree.insert ("f")    
    print()
    
    print('Height of the tree:', tree.height())
    print('Is the tree complete?', tree.complete())
    print()
    
    print('Adding "p" to the tree...')
    tree.insert ("p")
    print('Adding "q" to the tree...')
    tree.insert ("q")    
    print()    
    
    print('Height of the tree:', tree.height())
    print('Is the tree complete?', tree.complete())
    print()
    
    tree2 = MyBSTree() 
    
    print()
    print('Starting new tree...')
    print()
    
    print('Adding "z" to the list...') #this tree will test the new functions if there is only one item in the tree
    tree2.insert("z")
    print()
    
    print('Minimum value:', tree2.min())
    print('Maximum value:', tree2.max()) 
    print()
    
    print('Number of leaves in the tree:', tree2.numOfLeaves())
    print('Height of the tree:', tree2.height())
    print('Is the tree complete?', tree2.complete())
    print()    
    
    tree3 = MyBSTree() #test with an empty tree
    
    print()
    print('Starting new tree...')
    print()   
    
    try:
        print('Minimum value:', tree3.min())
    except BSTreeException as e:
        print('Got this error from trying to find the min of an empty tree') 
    try:
        print('Maximum value:', tree3.max()) 
    except BSTreeException as e:
        print('Got this error from trying to find the max of en empty tree')
    print()

    print('Number of leaves in the tree:', tree3.numOfLeaves())
    print('Height of the tree:', tree3.height())
    print('Is the tree complete?', tree3.complete())
    print()        
    
main()   