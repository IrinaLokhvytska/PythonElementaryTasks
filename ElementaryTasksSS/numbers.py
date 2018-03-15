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
    2: 'тысяч',
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
    end = 'надцать'
    dozens = list()
    helper = {
      0: 'десять',
      1: simple_number[1] + end,
      2: simple_number[2][:-1] + 'у' + end,
      3: simple_number[3] + end
    }
    for y in range(10):
      if y in helper:
        dozens.append(helper[y])
      else:
        dozens.append(simple_number[y][:-1] + end)
    dict_numbers[i].append(dozens)

def complete_dozen(i):
    helper = {
      2: simple_number[2] +'дцать',
      3: simple_number[3] +'дцать',
      4: 'сорок'
    }
    if i in helper:
      dict_numbers[i].append(helper[i])
    elif i == 1:
        complete_dozen_for_one(i)
    else:
        dict_numbers[i].append(simple_number[i] + 'десят')

def complete_hundred(i):
    helper = {
      1: 'сто',
      2: simple_number[2][:-1] + 'есте',
      3: simple_number[3] + 'ста',
      4: simple_number[4] + 'ста'
    }
    if i in helper:
        dict_numbers[i].append(helper[i])
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
          output += add_clarification(i, length)
          length -= 1
              
    return output
    
def add_clarification(n, l):
  output = ' '
  if l == 2:
     output += check_end_of_thousand(n, l) + ' '
  elif l > 2:
    output += n + ' ' + check_end_of_string(n, l) +' '
  else:
    output += n
  return output  
  
def check_end_of_thousand(n, l):
  output = ''
  ends = {'один': 'одна', 'два': 'две'}
  helper = {'один': 'а', 'два': 'и', 'три': 'и', 'четыре': 'и'}
  output = ''
  if n in ends:
    output +=  ends[n]
  else:
    output +=  n
  if n in helper:
    output += ' ' + number_clarification[l] + helper[n] + ' '
  else:
    output += ' ' + number_clarification[l] + ' '
  return output  

def check_end_of_string(n, l):
  output = ''
  helper = {'один': '', 'два': 'а', 'три': 'а', 'четыре': 'а'}
  if n in helper:
    output += ' ' + number_clarification[l] + helper[n] + ' '
  else:
    output += ' ' + number_clarification[l] + 'ов'
  return output   
  
print(show_result('455'))
