'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 4a
ID#: 1325352

This program tests the class Scores and its methods get, set, getNumOfScores, getTotalPoints, getAverage, getMaxValue, and getMinValue.

'''

from Scores import *

def main():
    
    score1 = Scores(10)
    
    try:
        score1.setScore(1, 99)
        score1.setScore(2, 201)
        score1.setScore(2, 76)
        score1.setScore(3, 150)
        score1.setScore(4, 200)
        score1.setScore(5, 78)
        score1.setScore(7, 100)
        score1.setScore(8, 82)
        score1.setScore(10, 127)
        score1.setScore(11, 89)
        
    except ScoresIllegalLabError as error:
        print('ScoresIllegalLabError: index out of range')
        
    print()
        
    try:
        print('Lab 1 score:', score1.getScore(1))
        print('Lab 2 score:', score1.getScore(2))
        print('Lab 3 score:', score1.getScore(3))
        print('Lab 4 score:', score1.getScore(4))
        print('Lab 5 score:', score1.getScore(5))
        print('Lab 7 score:', score1.getScore(7))
        print('Lab 8 score:', score1.getScore(8))
        print('Lab 10 score:', score1.getScore(10))
        print('Lab 11 score:', score1.getScore(11))
        
    except ScoresIllegalLabError as error:
        print('ScoresIllegalLabError: index out of range')
        
    print()
        
    print('Number of scores:', score1.getNumOfScores())
    
    print('Total of scores:', score1.getTotalPoints())
    
    print('Max value:', score1.getMaxValue())
    
    print('Min value:', score1.getMinValue())
    
    print('Average:', score1.getAverage())
        
main()