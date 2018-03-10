namespace = {'global': {'parent': 'None', 'vars': list()}}
def add(namesp, arg):
    namespace[namesp]['vars'].append(arg)

def create(namesp, arg):
    namespace[namesp] = {}
    namespace[namesp]['vars'] = list()
    namespace[namesp]['parent'] = arg

def get(namesp, arg):
    if arg in namespace[namesp]['vars']:
        return namesp
    else:
        if namespace[namesp]['parent'] != 'None':
            return get(namespace[namesp]['parent'], arg)

n = int(input())
for _ in range (n):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
    else:
        print(get(namesp, arg))

'''
inputs:
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
'''