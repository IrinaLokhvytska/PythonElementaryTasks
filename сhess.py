''' Print the chess board'''

def showChess (width, height, char):
    '''Print the chess board '''
    i = 0
    output = ''
    while i < abs(int(height)):
        j = 0
        while j < abs(int(width)):
            if i % 2 == 0:
                output += (char + ' ')
            else:
            	output += ( ' ' + char)
            j += 1
        output += '\n'
        i += 1
    return output

def validation (width, height, char):
    '''Validate values'''
    if checkEmptyValue (width) and checkNumbers (width):
        if checkEmptyValue (height) and checkNumbers (height):
            if checkEmptyValue (char):
                return showChess (width, height, char)
            else:
                print('Char can not be empty')
        else:
            print('The height of the chess should be a positive integer')
    else:  print('The width of the chess should be a positive integer')


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

width = input('Enter the width of the chess board: ')
height = input('Enter the height of the chess board: ')
char = input('Enter the char of the chess board: ')
print(validation (width, height, char))
