'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 9
ID#: 1325352

This program tests the functionality of the class Deque by adding, 
removing, and peeking from deques with more than one item, only one item,
or no items at all.

'''

from Deque import *

def main():
    
    print()
    print('Starting new deque...')
    print()    
    deque1 = Deque()
    
    print('Add "a" to the front of the deque:', deque1.addFront('a'))
    print('Add "b" to the front of the deque:', deque1.addFront('b'))
    print()
    
    print('Peeking front:', deque1.peekFront())
    print('Peeking back:', deque1.peekBack())
    print()    
    
    print('Add "c" to the back of the deque:', deque1.addBack('c'))
    print('Add "d" to the back of the deque:', deque1.addBack('d'))
    print()
    
    print('Remove the first item in the deque:', deque1.removeFront())
    print('Remove the last item in the deque:', deque1.removeBack()) 
    print()
    
    print('Is "a" in the deque?', deque1.isInDeque('a'))
    print('Is "c" in the deque?', deque1.isInDeque('c'))
    print('Is "d" in the deque?', deque1.isInDeque('d'))
    print()
    
    
    print()
    print('Starting new deque...')
    print()
    deque2 = Deque()
    
    print('Adding "one" to the back of the deque:', deque2.addBack('one'))
    print()
    
    print('Peeking front:', deque2.peekFront())
    print('Peeking back:', deque2.peekBack())
    print()
    
    print('Remove the first item in the deque:', deque2.removeFront())
    print()
    
    print('Adding "one" to the back of the deque:', deque2.addBack('one'))
    print()    
    
    print('Remove the last item in the deque:', deque2.removeBack())
    print()
    
    print()
    print('Starting new deque...')
    print()    
    deque3 = Deque()
    
    print('Add "a" to the back of the deque:', deque3.addBack('a'))
    print('Add "b" to the back of the deque:', deque3.addBack('b'))
    print('Add "c" to the back of the deque:', deque3.addBack('c'))  
    print('Add "d" to the back of the deque:', deque3.addBack('d'))
    print('Add "e" to the back of the deque:', deque3.addBack('e'))    
    print('Add "f" to the back of the deque:', deque3.addBack('f'))
    print('Add "g" to the back of the deque:', deque3.addBack('g'))    
    print()
    
    print('Peeking front:', deque3.peekFront())
    print('Peeking back:', deque3.peekBack())
    print()
    
    print('Remove the first item in the deque:', deque3.removeFront())
    print('Remove the last item in the deque:', deque3.removeBack())
    print('Remove "d" from the deque:', deque3.removeItem('d'))
    print()
    
    print('Is "a" in the deque?', deque3.isInDeque('a'))
    print('Is "b" in the deque?', deque3.isInDeque('b'))  
    print('Is "f" in the deque?', deque3.isInDeque('f'))    
    print('Is "g" in the deque?', deque3.isInDeque('g'))
    print('Is "d" in the deque?', deque3.isInDeque('d'))
    print()
    
    
    print()
    print('Starting new deque...')
    print()
    deque4 = Deque()
    
    try:
        print('Peeking front:', deque4.peekFront())
    except DequeException as e:
        print('Got this error from trying to peek from an empty deque')
        
    try:
        print('Peeking back:', deque4.peekBack())
    except DequeException as e:
        print('Got this error from trying to peek from an empty deque')
        
    try:
        print('Remove the first item in the deque:', deque4.removeFront())
    except DequeException as e:
        print('Got this error from trying to remove an item from an empty deque')
            
    try:
        print('Remove the last item in the deque:', deque4.removeBack())
    except DequeException as e:
        print('Got this error from trying to remove an item from an empty deque')
        
    print()
        
main()