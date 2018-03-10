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
    envelopes = {
    'The first side of the first envelope': a,
    'The second side of the first envelope': b,
    'The first side of the second envelope': c,
    'The second side of the second envelope': d
    }
    validation = checkEnvelopesValue(envelopes)
    if validation['valid'] == 4:
        return comparisonEnvelopes(a, b, c, d)
    else:
        return validation['msg']

def checkEnvelopesValue(envelopes):
    valid = 0
    msg = ''
    for key, value in envelopes.items():
        if checkEmptyValue(value):
            if checkPositiveNumbers(value):
                valid += 1
            else:
                msg += key + ' is not a positive integer: ' + value + '\n'
        else:
            msg += key + ' can not be empty \n'
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

a = input('Enter the first side of the first envelope: ')
b = input('Enter the second side of the first envelope: ')
c = input('Enter the first side of the second envelope: ')
d = input('Enter the second side of the second envelope: ')
print(validation (a, b, c, d))