'''Check that triangle exists and return its square'''
import math

def getSquare (name, side1, side2, side3):
    '''Get square of the triangle'''
    p = 0.5*(side1 + side2 + side3)
    square = math.sqrt((p*(p-side1)*(p-side2)*(p-side3)))
    output = {name : square}
    return output

def checkThatTriangleExists(side1, side2, side3):
    '''Check side of the triangle for existence'''
    exist = False
    if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side3 + side2 >= side1):
        exist = True
    return exist

def validation (name, side1, side2, side3):
    '''Validate values'''
    triangle = {'name': name, 'side1': side1, 'side2': side2, 'side3': side3}
    validation = checkTriangleValues(triangle)
    if validation['valid'] == 7:
        if checkThatTriangleExists(int(side1), int(side2), int(side3)):
            return getSquare (name, int(side1), int(side2), int(side3))
        else:
            return 'The triangle ' + name + ' does not exist'
    else:
        return validation['msg']

def checkTriangleValues(triangle):
    valid = 0
    msg = ''
    for key, value in triangle.items():
        if checkEmptyValue(value):
            if key != 'name':
                if checkPositiveNumbers(value):
                    valid += 1
                else:
                    msg += 'The ' + key + ' of the triangle is not a positive integer: ' + value + '\n'
            valid += 1
        else:
            msg += 'The ' + key + ' of the triangle can not be empty \n'
    output = {'valid' : valid, 'msg': msg}
    return output


def checkEmptyValue (value):
    '''Check that input value isn't empty'''
    validation = False
    if value:
        validation = True
    return validation

def checkPositiveNumbers (value):
     '''Check that input value can be converted to integer'''
     validation = False
     try:
         int(value)
     except ValueError:
         return validation
     if int(value) > 0:
         validation = True
     return validation

name = input('Enter the name of the triangle: ')
side1 = input('Enter the side1 of the triangle: ')
side2 = input('Enter the side2 of the triangle: ')
side3 = input('Enter the side3 of the triangle: ')
print(validation (name, side1, side2, side3))