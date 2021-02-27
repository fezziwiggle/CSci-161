'''
Maezy Haldeman: m.haldeman@und.edu
CS161: CompSci 2
Midterm Lab Exam
ID#: 1325352

'''
from Car import *

def main():
    
    car1 = Car('RAV4', 2010, 97000)
    print('getModel:', car1.getModel())    
    print('getYear:', car1.getYear())   
    print('getMileage:', car1.getMileage())  
    
    print()
    print()
    
    car2 = Car()
    
    print('setModel:', car2.setModel('Highlander'))
    print('setYear:', car2.setYear(2008))
    print('setMileage:', car2.setMileage(100000))
    
    print()
    
    print('getModel:', car2.getModel())
    print('getYear:', car2.getYear())
    print('getMileage:', car2.getMileage())
    
    print()
    print()    
    
    car3 = Car() #will create a car with "no info"
    
    print('setModel:', car3.setModel('Tundra'))
    print('setYear:', car3.setYear(2010))
    print('setMileage:', car3.setMileage(130000))  
    
    print()
    
    print('getModel:', car3.getModel())
    print('getYear:', car3.getYear())
    print('getMileage:', car3.getMileage())    
    
    print()
    print()    
    
    car4 = Car()
    
    print('setModel:', car4.setModel('Tacoma'))
    print('setYear:', car4.setYear(2020))
    print('setMileage:', car4.setMileage(1000001))  
    
    print()
    
    print('getModel:', car4.getModel())
    print('getYear:', car4.getYear())
    print('getMileage:', car4.getMileage())  
    
    print()
    print()    
    
    print('car1:', car1)
    
    print()
    
    print('car2:', car2)
    
    print()

    print('car3:', car3)

    print()

    print('car4:', car4)
    
    print()  
    print()    
    
    print('car4 equals car2:', car4.equals(car2)) 
    
    car4.setModel('Highlander')
    car4.setYear(2008)
    car4.setMileage(100000) 
    print()
    
    print('car4 equals car2:', car4.equals(car2))
    
    print()
    print()
    
    print('car1 highMileage:', car1.highMileage())
    
    print()
    
    print('car3 highMileage:', car3.highMileage())
    
    
main()