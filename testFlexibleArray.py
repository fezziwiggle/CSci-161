'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 3a
ID#: 1325352

This program tests the class FlexibleArray and its methods:
get, set, lowIndex, highIndex, indexOf and isInList.

'''
from FlexibleArray import FlexibleArray

def main():
    
    birthdays = FlexibleArray(1980, 2020)
    
    print(birthdays.lowIndex())
    print(birthdays.highIndex())
    
    try:
        birthdays.set(2002, 'Maezy')
        birthdays.set(1995, 'Maddy')
        birthdays.set(2018, 'Lily')
        birthdays.set(2016, 'Indy')
        birthdays.set(1979, 'Abba') #error check
    
    except Exception as error:
        print('Got this error from trying to set a value with an out-of-range index')
        
    print()
    
    try:  
        print(birthdays.get(2002))
        print(birthdays.get(1995))
        print(birthdays.get(2018))
        print(birthdays.get(2016))
        print(birthdays.get(2000)) #error check  
    
    except Exception as error:
        print('Got this error from trying to get a value using an out-of-range index')
        
    print()
    
    print(birthdays.isInList('Maddy'))
    print(birthdays.isInList('Bella')) #error check
    
    print()
    
    try:
        print(birthdays.indexOf('Maddy'))
        print(birthdays.indexOf('Bella')) #error check
        
    
    except Exception as error:
        print('Got this error from trying to find the index of an item not in the list')
        
    print()

        
main()