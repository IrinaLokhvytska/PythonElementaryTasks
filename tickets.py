'''Get the lucky tickets by 2 ways'''

def addZero(n):
    if n < 10:
        n = '00000' + str(n)
    elif n >= 10 and n < 100:
        n = '0000' + str(n)
    elif n >= 100 and n < 1000:
        n = '000' + str(n)
    elif n >= 1000 and n < 10000:
        n = '00' + str(n)
    elif n >= 10000 and n < 100000:
        n = '0' + str(n)
    elif n >= 100000 and n < 1000000:
        n = str(n)
    else:
        n = False
    return n

def helper(arr):
    result = 0
    odd = 0
    even = 0
    sum = 0
    for i in arr:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    if odd == even:
        result = 1
    return result

def easyWay(min, max):
    n = int(min)
    result = 0
    while n <= int(max):
        first = 0
        second = 0
        n = addZero(n)
        if (n):
            for i in list(n[:3]):
                first += int(i)
            for i in list(n[3:]):
                second += int(i)
            if (first == second):
                result += 1
        n = int(n) + 1
    return result

def hardWay(min, max):
    n = int(min)
    result = 0
    while n <= int(max):
        n = addZero(n)
        arr = list(n)
        result += helper(arr)
        n = int(n) + 1
    return result

def luckyTickets(min, max):
    easy = easyWay(min, max)
    hard = hardWay(min, max)
    msg = ''
    if easy > hard:
        msg = 'A simple method won. Simple: ' + str(easy) + ' Hard: ' + str(hard)
    elif hard > easy:
        msg = 'A hard method won. Simple: ' + str(easy) + ' Hard: ' + str(hard)
    elif easy == hard:
        msg = 'The methods are equal. Simple: ' + str(easy) + ' Hard: ' + str(hard)
    else:
        msg = 'In this range there are no lucky tickets.'
    return msg

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

def validation (min, max):
    '''Validate values'''
    if checkEmptyValue (min) and checkNumbers (min):
        if checkEmptyValue (max) and checkNumbers (max):
            if int(max) > int(min):
                return luckyTickets(min, max)
            else:
                print('The max value should be greater than min value')
        else:
            print('The max value should be a positive integer')
    else:  print('The min value should be a positive integer')

min = input('Enter the min value: ')
max = input('Enter the max value: ')
print(validation (min, max))