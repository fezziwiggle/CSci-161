'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 5b
ID#: 1325352

This program tests all the funtionality of the class LimitedStack by adding and removing items to 
both empty and full stacks.

'''

from LimitedStack import *

def main():
    
    stack1 = LimitedStack(5)
    
    stack1.push('x')
    stack1.push('y')
    stack1.push('z')
    
    print()
    
    print('Is stack1 empty?', stack1.isEmpty())
    print('Is stack1 full?', stack1.isFull())
    
    print()
    
    print(stack1)
    
    while not stack1.isEmpty():
        print('Removing from stack:', stack1.peek())
        stack1.top()
        print(stack1)                
        
    print()
    
    print('Is stack1 empty?', stack1.isEmpty())
    print('Is stack1 full?', stack1.isFull())
        
    print()
        
    stack1.push('a')
    stack1.push('b')
    stack1.push('c')
    stack1.push('d')
    stack1.push('e')
    stack1.push('f')
    stack1.push('g')
    stack1.push('h') 
    
    print()
    
    print('Is stack1 empty?', stack1.isEmpty())
    print('Is stack1 full?', stack1.isFull())
    
    print()
    
    print(stack1)
    
    while not stack1.isEmpty():
        print('Removing from stack:', stack1.peek())        
        stack1.top()
        print(stack1)        

    print()
    
    print('Is stack1 empty?', stack1.isEmpty())
    print('Is stack1 full?', stack1.isFull())    
    
    
    
    
main()