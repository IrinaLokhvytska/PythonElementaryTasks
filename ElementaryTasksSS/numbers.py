# -*- coding: utf-8 -*-

dict_numbers = dict()
simple_number = (
    'ноль',
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять'
)

def complete_dictionary():
    for i in range(10):
        dict_numbers[i] = list()
        dict_numbers[i].append(simple_number[i])
        complete_dozen(i)
        complete_hundred(i)
        if i > 1:
            complete_greater_dozen(i)

def complete_greater_dozen(i):
    if i in (2, 3):
        dict_numbers[i].append(simple_number[i] + 'дцать')
    elif i in range(5, 10):
        dict_numbers[i].append(simple_number[i] + 'десят')
    elif i == 4:
        dict_numbers[i].append('сорок')
    else:
        dict_numbers[i].append(simple_number[i][:-1] + str)

def complete_dozen(i):
    str = 'надцать'
    if i == 0:
        dict_numbers[i].append('десять')
    elif i in (1, 3):
        dict_numbers[i].append(simple_number[i] + str)
    elif i == 2:
        dict_numbers[i].append(simple_number[i][:-1] + 'е' + str)
    else:
        dict_numbers[i].append(simple_number[i][:-1] + str)

def complete_hundred(i):
    if i == 1:
        dict_numbers[i].append('сто')
    elif i == 2:
        dict_numbers[i].append(simple_number[i][:-1] + 'есте')
    elif i in (3, 4):
        dict_numbers[i].append(simple_number[i] + 'ста')
    else:
        dict_numbers[i].append(simple_number[i] + 'сот')

number_clarification = {
    (4, 7): 'тысяча',
    (7, 10): 'миллион',
    (10, 13): 'миллиард',
    (13, 16): 'триллион',
    (16, 19): 'квадриллион',
    (19, 22): 'квинтиллион',
    (22, 25): 'секстиллион',
    (25, 28): 'септиллион',
    (28, 31): 'октиллион',
    (31, 34): 'нониллион',
    (34, 37): 'дециллион'
    }

def get_simple_number(n):
    return simple_number[int(n)]

def get_from_ten_to_twenty(n):
    first, second = map(int, n)
    if second > 0:
        return dict_numbers[first][1]
    else:
        return dict_numbers[second][1]

def get_dozen_number(n):
    if int(n) in range (10, 20):
        return get_from_ten_to_twenty(n)
    elif int(n) in range(1, 10):
        return get_simple_number(n)
    else:
        return dict_numbers[int(n[0])][3] + ' ' + dict_numbers[int(n[1])][0]

def get_hundred_number(n):
    if int(n) in range (100, 1000):
        return dict_numbers[int(n[0])][2] + ' ' + get_dozen_number(n[1:])
    elif int(n) in range (10, 99):
        return get_dozen_number(n)
    else:
        get_simple_number(n)

def split_number(n):
    res = list()
    complete_dictionary()
    convert_function = ((get_hundred_number, 3), (get_simple_number, 1), (get_dozen_number, 2))
    while n:
        x = int(len(n)) % 3
        res.append(convert_function[x][0](n[0: convert_function[x][1]]))
        n = n[convert_function[x][1]:]
    return res

def show_result(n):
    length = len(split_number(n))

def validation(number):
    if check_empty_value(number) and check_numbers(number):
        split_number(number)
    else:
        pass

def check_empty_value(value):
    '''Check that input value isn't empty'''
    validation = False
    if value:
        validation = True
    return validation

def check_numbers(value):
     '''Check that input value can be converted to integer'''
     validation = False
     try:
         int(value)
     except ValueError:
         return validation
     if int(value) >= 0:
         validation = True
     return validation

number = input('Enter the number to convert: ')
