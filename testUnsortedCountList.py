'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 6b
ID#: 1325352

This program tests the class UnsortedCountList and all of its functions: add, remove, size, getNextItem, 
isFull, isEmpty, count, and overallCount.

'''

from UnsortedCountListLL import *

def main():
    
    list1 = UnsortedCountListLL(5)
    
    print('Add "Maezy" to list1:', list1.add('Maezy'))
    print('Add "Benjamin" to list1:', list1.add('Benjamin'))
    print('Add "Dassie" to list1:', list1.add('Dassie'))
    print('Add "Maezy to list1:', list1.add('Maezy'))
    print('Add "Lily" to list1:', list1.add('Lily'))
    print('Add "Indy" to list1:', list1.add('Indy'))
    print('Add "Maddy" to list1:', list1.add('Maddy'))
    
    print()
    
    for item in range (list1.size()):
        print (list1.getNextItem())  
    
    print()
    
    print('Size of list1:', list1.size())
    print('Overall count of list1:', list1.overallCount())
    print('Count of "Maezy" is list1:', list1.count('Maezy'))
    print('Count of "Benjamin" in list1:', list1.count('Benjamin'))
    print('"Maezy" in list1:', list1.isInList('Maezy'))
    print('"Maddy" in list1:', list1.isInList('Maddy'))
    print('"Dassie" in list1:', list1.isInList('Dassie'))
    
    print('isFull:', list1.isFull())
    print('isEmpty:', list1.isEmpty())
    
    print()
    
    print('Remove "Maezy" from list1:', list1.remove('Maezy'))
    print('Remove "Maezy from list1:', list1.remove('Maezy'))
    print('Remove "Maddy" from list1:', list1.remove('Maddy'))
    print('Remove "Dassie" from list1:', list1.remove('Dassie'))
    print('Remove "Indy" from list1:', list1.remove('Indy'))
    
    
    
    print()
    
    list1.reset()
    for item in range (list1.size()):
        print (list1.getNextItem())  
        
    print()
    
    print('Size of list1:', list1.size())
    print('Overall count of list1:', list1.overallCount())
    print('Count of "Maezy" in list1:', list1.count('Maezy'))
    print('Count of "Dassie" in list1:', list1.count('Dassie'))
    print('"Maezy" in list1:', list1.isInList('Maezy'))      
    print('isFull:', list1.isFull())
    print('isEmpty:', list1.isEmpty())
    print()
    
    
    
    list2 = UnsortedCountListLL()
    
    print('Add "Chopin" to list2:', list2.add('Chopin'))
    print('Add "Debussy" to list2:', list2.add('Debussy'))
    print('Add "Beethoven" to list2:', list2.add('Beethoven'))
    print('Add "Bach" to list2:', list2.add('Bach'))
    print('Add "Mozart" to list2:', list2.add('Mozart'))
    
    print()
    
    list2.reset()
    for item in range (list2.size()):
        print (list2.getNextItem())   
        
    print()
    
    print('Remove "Chopin" from list2:', list2.remove('Chopin'))
    print('Remove "Debussy" from list2:', list2.remove('Debussy'))
    print('Remove "Beethoven" from list2:', list2.remove('Beethoven'))
    print('Remove "Bach" from list2:', list2.remove('Bach'))
    print('Remove "Mozart" from list2:', list2.remove('Mozart'))  
    
    print()
    
    try:
        print (list2.getNextItem()) 
            
    except UnsortedCountListLLGetNextItemError as e:
        print('Got this error from trying to get next item from an empty linked list')


    
    
    
main()