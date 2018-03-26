import xml.etree.ElementTree as ET

xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
d = {'blue': 0, 'red': 0, 'green': 0}
root = ET.fromstring(xml)
d[root.attrib['color']] = 0
def detChild(root):
  for child in root:
    d[child.attrib['color']] += 1
    d[root.attrib['color']] += d[child.attrib['color']]
    detChild(child)
detChild(root)
    
print(d) 
