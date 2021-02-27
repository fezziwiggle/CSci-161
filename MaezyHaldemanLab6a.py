'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 6a
ID#: 1325352

This program asks the user to enter strings until the user enters an empty string. 
While the string is not empty, the program adds each character in the string 
to a queue and a list using ListQueue and ListStack. The program then removes and compares
the characters in the queue and stack one at a time, setting isPalindrome to True if all characters
match and setting isPalindrome to False otherwise.

'''

from ListQueue import *
from ListStack import *

def main():
    
    charQueue = ListQueue(100)
    charStack = ListStack(100)
    isPalindrome = False
    
    userString = input('Enter a string: ')
    
    while userString != '':
        for char in userString:
            charQueue.enqueue(char)
            charStack.push(char)
            
        print(charQueue)
        print(charStack)                
     
        for char in userString:        
            if charQueue.dequeue() == charStack.pop():
                isPalindrome = True
            else:
                isPalindrome = False
                break
        
        print('isPalindrome:', isPalindrome)    
        
        print()
        
        userString = input('Enter a string: ')    
        
    print()    
        
    print('Exiting program...')
                
                
main()
