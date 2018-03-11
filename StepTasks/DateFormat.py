import datetime

(y,m,d) = [int(n) for n in input().split()]
days = int(input())
future = datetime.date(y, m, d) + datetime.timedelta(days)

print(future.strftime("%Y %m %d").replace(' 0', ' '))

'''
2016 4 20
14
'''