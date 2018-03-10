n = int(input())
relationship = {}
for _ in range(n):
    classes = input()
    if classes.find(':') == -1:
        relationship[classes] = list()
    else:
        child, parent = classes.split(':')
        child = child.replace(' ', '')
        parent = parent.split()
        relationship[child] = parent
q = int(input())
for _ in range(q):
    query = input()
    parent, child = query.split()
    try:
        if parent in relationship[child]:
            print ('Yes')
    except Exception:
        print ('No')

'''
input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
'''