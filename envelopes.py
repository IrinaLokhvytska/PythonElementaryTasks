'''Comparison Envelopes'''

def comparisonEnvelopes(a, b, c, d):
    msg = ''
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if (a*b >= c*d) and ((a**2 + b**2) >= (c**2 + d**2)) and (a + b >= c + d) and (min([a, b]) >= min([c, d])):
        msg = 'The second envelope is placed in the first.'
    elif (c*d >= a*b) and ((c**2 + d**2) >= (a**2 + b**2)) and (c + d >= a + b) and (min([c, d]) >= min([a, b])):
        msg = 'The first envelope is placed in the second.'
    else:
        msg = 'Envelopes can not be placed in each other.'
    return msg

def validation (a, b, c, d):
    '''Validate values'''
    if checkEmptyValue (a) and checkNumbers (a):
        if checkEmptyValue (b) and checkNumbers (b):
            if checkEmptyValue (c) and checkNumbers (c):
                if checkEmptyValue (d) and checkNumbers (d):
                    return comparisonEnvelopes(a, b, c, d)
                else:
                    print('The second side of the second envelope should be a positive integer')
            else:
                print('The first side of the second envelope should be a positive integer')
        else:
            print('The second side of the first envelope should be a positive integer')
    else:  print('The first side of the first envelope should be a positive integer')

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

a = input('Enter the first side of the first envelope: ')
b = input('Enter the second side of the first envelope: ')
c = input('Enter the first side of the second envelope: ')
d = input('Enter the second side of the second envelope: ')
print(validation (a, b, c, d))