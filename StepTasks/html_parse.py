import requests
import re

def flatten(lst):
    return [y for x in lst for y in x]
    
A = input()
B = input()
pattern = '<a\s.*?href="(.+?)".*?>'
result = []
response = requests.get(A)
if response.status_code == 200:
  content = response.text
  links = re.findall(pattern, content)
  for link in links:
    req = requests.get(link)
    if req.status_code == 200:
      text = req.text
      result.append(re.findall(pattern, text))
result = flatten(result)
if B in result:
  print('Yes')
else:
  print('No')
