'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 1b Part 2
ID#: 1325352

This program opens an existing text file and reads the scores on each line to a list.
The list is then put through several functions where the program can then return
the the total, mean, median, and mode for all the scores in the opened file.

'''

import FileUtils
import os

#=======================================

def readFile(fileName):
    
    openFile = open(fileName, 'r')   
    fileList = []
    readToList = openFile.readlines()
    
    for item in readToList:
        fileList.append(int(item.strip()))
        
    openFile.close()
        
    return fileList

#---------------------------------------

def findMean(fileList):
    
    mean = 0
    sumValues = 0
    total = len(fileList)
    
    for item in fileList:
        sumValues += item
    
    mean = sumValues / total
    mean = format(mean, "1.2f")
    
    return mean
    
#---------------------------------------

def findMedian(fileList):
    
    fileList.sort()
    total = len(fileList)
    
    if total % 2 == 0:
        median1 = fileList[total//2] 
        median2 = fileList[total//2 - 1] 
        median = (median1 + median2)/2   
        
    else:
        median = fileList[total//2] 
        
    return median
    
#---------------------------------------

def findMode(fileList):
    
    fileDict = {}
    
    for number in fileList:
        
        if number in fileDict: #Increment count of character by 1 
            fileDict[number] = fileDict[number] + 1

        else: #Add the character to dictionary with count 1 
            fileDict[number] = 1     
    
    mode = max(fileDict.values())
    modeValues = [key for key in fileDict if fileDict[key] == mode]
    
    return modeValues
    
#---------------------------------------
             
def main():

    fileName = FileUtils.selectOpenFile()
    
    if fileName == None:
        print('No file selected. Exiting program...')
        os._exit(0)
        
    if os.path.isfile(fileName) == False:
        print("Entered file doesn't exist. Exiting program...")
    
    else:
        fileList = readFile(fileName)
        total = len(fileList)
        mean = findMean(fileList)
        median = findMedian(fileList)
        mode = findMode(fileList)
        
        print('Total:', total)
        print('Mean:', mean)
        print('Median:', median)
        print('Mode:', mode)

#=======================================

main()