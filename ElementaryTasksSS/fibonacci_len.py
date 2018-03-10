'''Fibonacci Numbers'''

def fib(min, length):
    minRange = minFib(int(min))
    a = minRange[0]
    b = minRange[1]
    result = [a]
    while len(result) < int(length):
        a, b = b, a+b
        result.append(a)
    return result

def minFib(min):
    a = 0
    b = 1
    while a < min:
        a, b = b, a + b
    return (a, b)

def validation (min, length):
    '''Validate values'''
    fibonacci = {'min': min, 'length': length}
    validation = checkFibonacciValues(fibonacci)
    if validation['valid'] == 2:
        return fib(min, length)
    else:
        return validation['msg']

def checkFibonacciValues(fibonacci):
    valid = 0
    msg = ''
    for key, value in fibonacci.items():
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

min = input('Enter the min value: ')
length = input('Enter the length value: ')
print(validation (min, length))