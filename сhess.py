''' Print the chess board'''

def showChess (width, height, char):
    '''Print the chess board '''
    i = 0
    output = ''
    while i < int(height):
        j = 0
        while j < int(width):
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
    valid = 0
    msg = ''
    chess = {'width': width, 'height': height, 'char': char}
    for key, value in chess.items():
        if checkEmptyValue(value):
            if key != 'char':
                if checkPositiveNumbers(value):
                    valid += 1
                else:
                    msg += 'The ' + key + ' of the chess should be a positive integer \n'
            valid += 1
        else:
            msg += 'The ' + key + ' of the chess can not be empty \n'
    if valid == 5:
        return showChess (width, height, char)
    else:
        return msg

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

width = input('Enter the width of the chess board: ')
height = input('Enter the height of the chess board: ')
char = input('Enter the char of the chess board: ')
print(validation (width, height, char))
