import re
import requests

html = input()
response = requests.get(html)
if response.status_code == 200:
  content = response.text
  urls = re.findall(r'''<a\s.*?href=['"]([\w\d-].+?)['"?]''', content)
domains = set()
for url in urls:
    if "//" in url:
        domain = url.split("//")[1].split("/")[0].split('?')[0].split(':')[0]
    else:
        domain = url.split("//")[-1].split("/")[0].split('?')[0].split(':')[0]
    domains.add(domain)
output = list(domains)
output.sort()
for el in output:
    print(el)
