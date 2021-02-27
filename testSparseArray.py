'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 7a
ID#: 1325352

This program tests the functionality of the SparseArray class by creating a sparse array
with the desired max row/col values and adding, removing, and updating nodes from the array.

'''

from SparseArray import *

def main():
    
    array1 = SparseArray(None, 100, 100)
    defaultValue = array1.getDefaultValue()
    print('Default value:', defaultValue)
    print()
    
     
    print('Setting node at 10, 20...') #row/col is valid and coordinates DO NOT reference an existing node
    array1.set(10, 20, 'Nelson')
    print('Node at 10, 20:', array1.get(10, 20))
    print()  
    
    print('Setting node at 30, 40...')
    array1.set(30, 40, 'Maezy')
    print('Node at 30, 40:', array1.get(30, 40))
    print()
    
    print('Setting node at 50, 60...')
    array1.set(50, 60, 'Indy')
    print('Node at 50, 60:', array1.get(50, 60))
    print()
    
    print('Updating node at 50, 60...') #row/col are coordinates of an existing node, so update that node's value
    array1.set(50, 60, 'Lily') 
    print('Node at 50, 60:', array1.get(50, 60))  
    print()
    
    print('Updating node at 50, 60...') #row/col are coordinates of an existing node, so update that node's value
    array1.set(50, 60, 'Fezziwiggle') 
    print('Node at 50, 60:', array1.get(50, 60))  
    print()    
    
    print('Resetting node at 50, 60...') #either row or col is the default value, so reset row, col, and value to default value, essentially "resetting" that node
    array1.set(50, 60, defaultValue)
    print('Node at 50, 60:', array1.get(50, 60))
    print()
    
    print('Node at 10, 10:', array1.get(10, 10)) #row/col are not coordinates of any existing node, so return default value 
    print()    
        
    try:
        print('Setting node at 101, 101...') #row/col are out of range, so raise an exception
        array1.set(101, 101, 'Maddy')
        print('Node at 101, 101:', array1.get(101, 101))
        print()
        
    except SparseArrayException as e:
        print('Got this error from trying to set a node outside of range')
        print()
        
    try:
        print('Setting node at 70, 80...') #row/col are valid coordinates, but you can't set a new node with default value
        array1.set(70, 80, defaultValue)
        print('Node at 70, 80:', array1.get(70, 80))
        print()
    
    except SparseArrayException as e:
        print('Got this error from trying to set a non-existing node with the default value')
        print()

    
main()