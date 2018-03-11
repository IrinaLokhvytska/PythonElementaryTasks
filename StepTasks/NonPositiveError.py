class NonPositiveError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError(x, 'Element must be greater than 0')
        else:
            super(PositiveList, self).append(x)

l =  PositiveList([1,2])
l.append(5)
print(l)