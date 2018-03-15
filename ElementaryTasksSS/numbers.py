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


number_clarification = {
    2: 'тысяча',
    3: 'миллион',
    4: 'миллиард',
    5: 'триллион',
    6: 'квадриллион',
    7: 'квинтиллион',
    8: 'секстиллион',
    9: 'септиллион',
    10: 'октиллион',
    11: 'нониллион',
    12: 'дециллион'
    }

def complete_dictionary():
    for i in range(10):
        dict_numbers[i] = list()
        dict_numbers[i].append(simple_number[i])
        if i == 0:
            continue
        else:
            complete_dozen(i)
            complete_hundred(i)

def complete_dozen_for_one(i):
    str = 'надцать'
    dozens = list()
    for y in range(10):
        if y == 0:
            dozens.append('десять')
        elif y in (1, 3):
            dozens.append(simple_number[y] + str)
        elif y == 2:
            dozens.append(simple_number[y][:-1] + 'у' + str)
        else:
            dozens.append(simple_number[y][:-1] + str)
    dict_numbers[i].append(dozens)

def complete_dozen(i):
    if i == 1:
        complete_dozen_for_one(i)
    elif i in (2, 3):
        dict_numbers[i].append(simple_number[i] +'дцать')
    elif i == 4:
        dict_numbers[i].append('сорок')
    else:
        dict_numbers[i].append(simple_number[i] + 'десят')

def complete_hundred(i):
    if i == 1:
        dict_numbers[i].append('сто')
    elif i == 2:
        dict_numbers[i].append(simple_number[i][:-1] + 'есте')
    elif i in (3, 4):
        dict_numbers[i].append(simple_number[i] + 'ста')
    else:
        dict_numbers[i].append(simple_number[i] + 'сот')

def get_simple_number(n):
    return dict_numbers[int(n)][0]

def get_from_ten_to_twenty(n):
    first, second = map(int, n)
    return dict_numbers[first][1][second]

def get_dozen_number(n):
    if int(n) in range (10, 20):
        return get_from_ten_to_twenty(n)
    elif int(n) in range(1, 10):
        return get_simple_number(n)
    else:
        n = str(int(n))
        return dict_numbers[int(n[0])][1] + ' ' + dict_numbers[int(n[1])][0]

def get_hundred_number(n):
    if int(n) in range (100, 1000):
        return dict_numbers[int(n[0])][2] + ' ' + get_dozen_number(n[1:])
    elif int(n) in range (10, 99):
        return get_dozen_number(n)
    elif int(n) == 0:
        return '000'
    else:
        return get_simple_number(n)

def split_number(n):
    complete_dictionary()
    res = list()
    n_without_zero = str(int(n))
    convert_function = ((get_hundred_number, 3), (get_simple_number, 1), (get_dozen_number, 2))
    while n_without_zero:
        x = int(len(n_without_zero)) % 3
        res.append(convert_function[x][0](n_without_zero[0: convert_function[x][1]]))
        n_without_zero = n_without_zero[convert_function[x][1]:]
    return (res)

def show_result(n):
    numbers = split_number(n)
    length = int(len(numbers))
    output = ''
    for i in numbers:
        if i == '000':
            length -= 1
            continue
        else:
            output += i
            if length >= 2:
                output += ' ' + number_clarification[length] + ' '
                length -= 1
              
    return output

print(show_result('10125'))
