'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 4a
ID#: 1325352

This program creates a class that allows the user to store labs and their scores and perform a number of methods on the data (min, max, average). 
The get and set methods convert the user-perceived indeces (1 based) into list indeces (0 based) and vice versa.

'''

class ScoresIllegalLabError(Exception):
    pass


class Scores:
    
    NO_VALUE = -1
    
    
    def __init__(self, maxSize):
        
        self.__maxSize = maxSize
        self.__ourList = [Scores.NO_VALUE] * maxSize
        self.__numOfScores = 0
        self.__totalPoints = 0
        
        
        
    def setScore(self, index, score): #when setting a score in ourList, make sure score for Lab "1" is stored at index 0
        
        if index > self.__maxSize:
            raise ScoresIllegalLabError('Invalid index ', index, '')
        
        if 0 <= score <= 200 :
            ourIndex = (index - 1)
            self.__ourList[ourIndex] = score
            self.__numOfScores += 1
            self.__totalPoints += score
            return True
        
        else:
            return False

        
        
    def getScore(self, index): #when returning the score at the index, make sure the user index example 1 is turned into programmer index 0
        
        if index <= self.__maxSize:
            ourIndex = (index - 1)
            return self.__ourList[ourIndex]
            
        else:
            raise ScoresIllegalLabError('Invalid index ', index, '')
        
        
    def getNumOfScores(self):
        
        return self.__numOfScores
        
        
    def getTotalPoints(self):
        
        return self.__totalPoints
        
        
    def getMaxValue(self):
        
        maxValue = -1
        for ourIndex in range(0, self.__numOfScores):
            if self.__ourList[ourIndex] >= maxValue:
                maxValue = self.__ourList[ourIndex]
        return maxValue
        
        
    def getMinValue(self):
        
        minValue = self.__ourList[0]
        for ourIndex in range(0, self.__maxSize):
            if self.__ourList[ourIndex] != -1:
                if self.__ourList[ourIndex] <= minValue:
                
                    minValue = self.__ourList[ourIndex]
        return minValue
        
    def getAverage(self):
        
        if self.__numOfScores != 0:
            return (self.__totalPoints / self.__numOfScores)
        
        else:
            return Scores.NO_VALUE
