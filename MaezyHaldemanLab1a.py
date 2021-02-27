'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 1a
ID#: 1325352

This program displays a menu of options for converting degrees of tempurature
in Kelvin, Fahrenheit, and Celsius, and uses functions for conversions between each unit.

'''

#===========================================

def FtoC(fahr):    # Convert from Fahrenheit to Celsius
    
    celsius = (fahr - 32) * 5/9
    celsius = format(celsius, "1.2f")
    
    return celsius    
    
#-------------------------------------------
        
def FtoK(fahr):    # Convert from Fahrenheit to Kelvin

    kelvin = (fahr + 459.67) * 5/9
    kelvin = format(kelvin, "1.2f")
    
    return kelvin
    
#-------------------------------------------

def CtoK(celcius):    # Convert from Celsius to Kelvin
    
    kelvin = celcius + 273.15
    kelvin = format(kelvin, "1.2f") 
    
    return kelvin
        
#-------------------------------------------

def CtoF(celcius):    # Convert from Celsius to Fahrenheit

    fahr = celcius * 9/5 + 32
    fahr = format(fahr, "1.2f")
    
    return fahr
    
#-------------------------------------------

def KtoC(kelvin):    # Convert from Kelvin to Celsius

    celsius = kelvin - 273.15
    celsius = format(celsius, "1.2f")    
    
    return celsius
    
#-------------------------------------------
    
def KtoF(kelvin):    # Convert from Kelvin to Fahrenheit

    fahr = kelvin * 9/5 - 459.67
    fahr = format(fahr, "1.2f")    
    
    return fahr

#-------------------------------------------

def printMenu():    # display menu
    
    print('1)  Fahrenheit to Celsius')
    print('2)  Fahrenheit to Kelvin')
    print('3)  Celsius to Kelvin')
    print('4)  Celsius to Fahrenheit')
    print('5)  Kelvin to Celsius')
    print('6)  Kelvin to Fahrenheit')
    print('7)  Quit')    
    
#-------------------------------------------

def getMenuChoice():    # get user's choice
    
    printMenu()
    print()
    menuChoice = int(input('Selection: '))
    print()
    
    while menuChoice < 1 or menuChoice > 7:
        
        print('Please enter a valid menu option (1-7)')
        print()
        menuChoice = int(input('Selection: '))
        
    return menuChoice

#-------------------------------------------

    
#*******************************************  
    
def main():
    
    print()
    print('Menu')
    print()
    userChoice = getMenuChoice()
    
    while userChoice != 7:
        
        if userChoice == 1: # Convert from Fahrenheit to Celsius
            
            fahr = int(input('Fahrenheit tempurature: '))
            fahrToCels = FtoC(fahr)
            print(fahr, 'degrees Fahrenheit is', fahrToCels, 'degrees Celsius')
            print()
            
        elif userChoice == 2: # Convert from Fahrenheit to Kelvin
            
            fahr = int(input('Fahrenheit tempurature: '))
            fahrToKelv = FtoK(fahr)
            print(fahr, 'degrees Fahrenheit is', fahrToKelv, 'degrees Kelvin')            
            print()
            
        elif userChoice == 3: # Convert from Celsius to Kelvin
            
            celsius = int(input('Celsius tempurature: '))  
            celsToKelv = CtoK(celsius)
            print(celsius, 'degrees Celsius is', celsToKelv, 'degrees Kelvin')            
            print()
            
        elif userChoice == 4: # Convert from Celsius to Fahrenheit
            
            celsius = int(input('Celsius tempurature: '))     
            celsToFahr = CtoF(celsius)
            print(celsius, 'degrees Celsius is', celsToFahr, 'degrees Fahrenheit')            
            print()
            
        elif userChoice == 5: # Convert from Kelvin to Celsius
            
            kelvin = int(input('Kelvin tempurature: '))    
            kelvToCels = KtoC(kelvin)
            print(kelvin, 'degrees Kelvin is', kelvToCels, 'degrees Celsius')            
            print()
    
        elif userChoice == 6: # Convert from Kelvin to Fahrenheit
            
            kelvin = int(input('Kelvin tempurature: '))
            kelvToFahr = KtoF(kelvin)
            print(kelvin, 'degrees Kelvin is', kelvToFahr, 'degrees Fahrenheit')            
            print()
            
        userChoice = getMenuChoice()
    
    if userChoice == 7:
        
        print('Exiting program...')
        
#*******************************************
               
main()
