'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 3b
ID#: 1325352

This program takes the original test program for UnsortedList and tests the new methods added in UnsortedList2,
replaceAll, removeAll, count, and partialMatch.

'''

from UnsortedList2 import UnsortedList2

def main ():

    ul1 = UnsortedList2(6)
    ul2 = UnsortedList2()  #defaults to 10 items

    try: #code that could crash the program can go into a try block
        ul1.add ("a")
        ul1.add ("b")
        ul1.add ("c")
        ul1.add ("d")
        ul1.add ("e")

        ul1.remove ("b")
        ul1.add ("f")
        ul1.add ("g")
        ul1.add ("h")
        ul1.add ("i")
        ul1.add ("j")
    except Exception as error:    
        #here is where we put the code to deal with the error 
        print ("Got this error from trying to add to much information to the list: ", error)

    if ul1.isInList ("c"):
        print ("c is in the list")
    else:
        print ("c is not in the list")

    if ul1.isInList ("b"):
        print ("b is in the list")
    else:
        print ("b is not in the list")

    ul1.reset()
    for x in range (ul1.size()):
        print (ul1.getNextItem() )

    for x in range (ul1.size()):
        print (ul1.getNextItem() )

    #for item in ul1:
    #   print (item)
    
    
#================================================================================

#BEGIN MY CODE HERE

#================================================================================
    
    print()
    print('Starting my own tests: ')
    print()
    
    ul2.add('a')
    ul2.add('b')
    ul2.add('c')
    ul2.add('d')
    ul2.add('d')
    ul2.add('e')
    ul2.add('f')
    ul2.add('g')
    
    print(ul2.removeAll('d'), 'occurences of "d" removed')
    
    print()
    
    ul2.reset()
    
    for x in range (ul2.size()):
        print(ul2.getNextItem())
        
    print()
        
    print((ul2.count('d')), 'occurences of "d" in the list')
    
    print()
    
    ul2.add('z')
    ul2.add('z')
    
    print(ul2.replaceAll('y', 'z'), 'occurences of "z" replaced with "y"')
    
    print()
          
    ul2.reset()
    
    for x in range (ul2.size()):
        print(ul2.getNextItem())
        
    ul3 = UnsortedList2()
    
    ul3.add('one')
    ul3.add('two')
    ul3.add('three')
    ul3.add('four')
    ul3.add('five')
    
    print()
    
    for x in range (ul3.size()):
        print(ul3.getNextItem())
        
    print()
    
    try:        
        name = ul3.partialMatch('o')
        while name != None:
            print('Partial match for "o":', name)
            name = ul3.partialMatch()
            
        ul3.reset()    
        print()
        
        name = ul3.partialMatch('e')
        while name != None:
            print('Partial match for "e":', name)
            name = ul3.partialMatch()    
        
        ul3.reset()
        print()
        
        name = ul3.partialMatch()
        print(name)
    
    except Exception as error:
        print('Got this error from not setting an initial search criteria in partialMatch')

main() 