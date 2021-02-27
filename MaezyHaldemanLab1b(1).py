'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 1b Part 1
ID#: 1325352

This program asks the user to select or create a new file, then 
prompts the user to enter scores 0-100 until they enter -1 to quit.
Every score is saved to a new line.

'''

import FileUtils
import os

#=======================================

def main():
    
    print('Select a file for writing: ')
    print()
    fileName = FileUtils.selectSaveFile()
    
    if fileName == None:
        print('No file selected. Exiting program...')
        os._exit(0)
        
    else:
        openFile = open(fileName, 'w')
        score = input('Enter a test score (0-100) or -1 to quit: ')
    
        while score != '-1' or score == '':
            
            if score == '':
                openFile.write(score + "\n")
                score = input('Enter a test score (0-100) or -1 to quit: ')                   
        
            elif 0 <= int(score) <= 100:
                openFile.write(score + "\n")
                score = input('Enter a test score (0-100) or -1 to quit: ')   
            
            else:
                print()
                print('That number is out of range')
                print()
                score = input('Enter a test score (0-100) or -1 to quit: ')   

        print()
        print('Exiting program...')
        openFile.close()
            
#=======================================

main()