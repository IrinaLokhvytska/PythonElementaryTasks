import urllib.request
import json

number = input()
link = 'http://numbersapi.com/'+number+'/math?json=true'
with urllib.request.urlopen(link) as url:
  data = json.loads(url.read().decode())
  if data['found']:
    print('Interesting')
  else:
    print('Boring')
    
# 960
# 994
# 900
# 937
# 909
# 944
# 978
# 915
# 948
# 918
# 983
# 921
# 954
# 989
# 958
