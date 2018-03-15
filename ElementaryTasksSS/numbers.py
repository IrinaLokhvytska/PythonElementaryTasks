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
    12: 'дециллион',
    13: 'ундециллион',
    14: 'додециллион',
    15: 'тредециллион',
    16: 'кваттуордециллион',
    17: 'квиндециллион',
    18: 'cедециллион',
    19: 'септдециллион',
    20: 'дуодевигинтиллион',
    21: 'ундевигинтиллион',
    22: 'вигинтиллион',
    23: 'анвигинтиллион',
    24: 'дуовигинтиллион',
    25: 'тревигинтиллион',
    26: 'кватторвигинтиллион',
    27: 'квинвигинтиллион',
    28: 'сексвигинтиллион',
    29: 'септемвигинтиллион',
    30: 'октовигинтиллион',
    31: 'новемвигинтиллион',
    32: 'тригинтиллион',
    33: 'антригинтиллион'
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
      2: simple_number[2][:-1] + 'е' + end,
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
      4: 'сорок',
      9: simple_number[9][:-2] + 'носто'
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
      2: simple_number[2][:-1] + 'ести',
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

def get_dozen_dict(n):
    first, second = map(int, n)
    if first and second != 0:
      return dict_numbers[first][1] + ' ' + dict_numbers[second][0]
    else:
      return dict_numbers[first][1]

def get_dozen_number(n):
    num_range = {
      get_simple_number: [1, 10], 
      get_from_ten_to_twenty: [10, 20],
      get_dozen_dict: [20, 100]
    }
    for key, value in num_range.items():
      if int(n) in range (value[0], value[1]):
        return  key(n)
    return ''

def get_hundread_dict(n):
    return dict_numbers[int(n[0])][2] + ' ' + get_dozen_number(n[1:])

def get_hundred_number(n):
    num_range = {
      get_simple_number: [1, 10], 
      get_dozen_number: [10, 100], 
      get_hundread_dict: [100, 1000]}
    for key, value in num_range.items():
      if int(n) in range (value[0], value[1]):
        return  key(n)
    return '000'

def split_number(n):
    complete_dictionary()
    res = list()
    n_without_zero = str(int(n))
    convert_function = ((get_hundred_number, 3), (get_simple_number, 1), (get_dozen_number, 2))
    while n_without_zero:
        x = int(len(n_without_zero)) % 3
        slice_num = convert_function[x][1]
        res.append(convert_function[x][0](n_without_zero[0: slice_num]))
        n_without_zero = n_without_zero[slice_num:]
    return (res)

def show_result(n):
    numbers = split_number(n)
    length = int(len(numbers))
    if length > 33:
      return 'The number too big'
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
  output = ''
  if l == 2:
     output += check_end_of_thousand(n, l) + ' '
  elif l > 2:
    output += n + ' ' + check_end_of_string(n, l) +' '
  else:
    output += n
  return output  
  
def check_end_of_thousand(n, l):
  ends = {
    'один': ('а', 'одна', 4), 
    'два': ('и', 'две', 3), 
    'три': ('и', 'три', 3), 
    'четыре': ('и', 'четыре', 6)
    
  }
  for k in ends:
    if k in n.split(' ')[-1:][0]:
      return n[:-ends[k][2]] + ends[k][1] + ' ' + number_clarification[l] + ends[k][0] 
  return n + ' ' + number_clarification[l]

def check_end_of_string(n, l):
  ends = {'один': '', 'два': 'а', 'три': 'а', 'четыре': 'а'}
  for k in ends:
    if k in n.split(' ')[-1:][0]:
      return number_clarification[l] + ends[k] 
  return number_clarification[l] + 'ов'
  
print(show_result('1157895698741238155545545000005'))
