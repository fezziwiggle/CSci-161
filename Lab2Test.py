'''
Maezy Haldeman

test program for class HonorPoints

'''

from HonorPoints import HonorPoints

def main():
    
    Maezy = HonorPoints() 
    Benjamin = HonorPoints('Benjamin')   
    
    Maezy.setName('Maezy H.')
    Maezy.addClass(4, 'A')
    Maezy.addClass(3, 'b')
    Maezy.addClass(5, 'a')
    Maezy.addClass(5, 'A')
    Maezy.addClass(4, 'B')
    
    print('Name:                ', Maezy.getName())
    print('Total credits:       ', Maezy.getCredits())
    print('Total passed credits:', Maezy.getPassedCredits())
    print('Total honor points:  ', Maezy.getHonorPoints())
    print('GPA:                 ', format(Maezy.getGPA(), "1.3f"))
    
    print()
    
    Benjamin.setName('Benjamin H.')
    Benjamin.addClass(4, 'A')
    Benjamin.addClass(3, 'b')
    Benjamin.addClass(5, 'B')
    
    print('Name:                ', Benjamin.getName())
    print('Total credits:       ', Benjamin.getCredits())
    print('Total passed credits:', Benjamin.getPassedCredits())
    print('Total honor points:  ', Benjamin.getHonorPoints())
    print('GPA:                 ', format(Benjamin.getGPA(), "1.3f"))    
    
    print()
        
    if Maezy.isSmarter(Benjamin):
        print('Maezy is smarter than Benjamin')
    else:
        print('Benjamin is smarter than Maezy')
    
    if Maezy.canGraduate():
        print('Maezy has enough credits to graduate')
    else:
        print('Maezy does not have enough credits to graduate')
        
    if Benjamin.canGraduate():
        print('Benjamin has enough credits to graduate')
    else:
        print('Benjamin does not have enough credits to graduate')    

main()