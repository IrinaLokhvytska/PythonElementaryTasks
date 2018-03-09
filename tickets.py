'''Get the lucky tickets by 2 ways'''

def addZero(n):
    ticketsRange = {
    '00000': [0, 10],
    '0000': [10, 100],
    '000': [100, 1000],
    '00': [1000, 10000],
    '0': [10000, 100000],
    '': [100000, 1000000]
    }
    for key, value in ticketsRange.items():
        if int(n) in range (value[0], value[1]):
            n = str(n) + key
    return n

def helper(arr):
    result = odd = even = sum = 0
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
        first = second = 0
        n = addZero(n)
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

def checkNumbers(value):
     '''Check that input value can be converted to integer'''
     try:
         int(value)
     except ValueError:
         return False
     return True

def checkTicketsRange(value):
    validation = False
    if int(value) >= 0 and int(value) < 1000000:
        validation = True
    return validation

def validation (min, max):
    '''Validate values'''
    tickets = {'min': min, 'max': max}
    validation = checkTicketsValues(tickets)
    if validation['valid'] == 2:
        if int(max) > int(min):
            return luckyTickets(min, max)
        else:
            return 'The max value should be greater than min value'
    else:
        return validation['msg']

def checkTicketsValues(tickets):
    valid = 0
    msg = ''
    for key, value in tickets.items():
        if checkEmptyValue(value):
            if checkNumbers(value):
                if checkTicketsRange(value):
                    valid += 1
                else:
                    msg += 'The ' + key + ' is not in range [0:1000000]: ' + value + '\n'
            else:
                 msg += 'The ' + key + ' is not a positive integer: ' + value + '\n'
        else:
            msg += 'The ' + key + ' can not be empty \n'
    output = {'valid': valid, 'msg': msg}
    return output

min = input('Enter the min value: ')
max = input('Enter the max value: ')
print(validation (min, max))