'''Check that triangle exists and return its square'''
import math

def getSquare (name, side1, side2, side3):
    '''Get square of the triangle'''
    p = 0.5*(int(side1) + int(side2) + int(side3))
    square = math.sqrt((p*(p-int(side1))*(p-int(side2))*(p-int(side3))))
    output = {name : square}
    return output

def checkThatTriangleExists(side1, side2, side3):
    '''Check side of the triangle for existence'''
    exist = False
    if (int(side1) + int(side2) >= int(side3)) and (int(side1) + int(side3) >= int(side2)) and (int(side3) + int(side2) >= int(side1)):
        exist = True
    return exist

def validation (name, side1, side2, side3):
    '''Validate values'''
    if checkEmptyValue (side1) and checkNumbers (side1):
        if checkEmptyValue (side2) and checkNumbers (side2):
            if checkEmptyValue (side3) and checkNumbers (side3):
                if checkEmptyValue (name):
                    if checkThatTriangleExists(side1, side2, side3):
                        return getSquare (name, side1, side2, side3)
                    else:
                        print('The triangle ' + name + ' does not exist')
                else:
                    print('Name can not be empty')
            else:
                print('The side3 of the triangle should be a positive integer')
        else:  print('The side2 of the triangle should be a positive integer')
    else:  print('The side1 of the triangle should be a positive integer')

def checkEmptyValue (value):
    '''Check that input value isn't empty'''
    validation = False
    if value:
        validation = True
    return validation

def checkNumbers (value):
     '''Check that input value can be converted to integer'''
     try:
         int(value)
     except ValueError:
         return False
     return True

name = input('Enter the name of the triangle: ')
side1 = input('Enter the side1 of the triangle: ')
side2 = input('Enter the side2 of the triangle: ')
side3 = input('Enter the side3 of the triangle: ')
print(validation (name, side1, side2, side3))