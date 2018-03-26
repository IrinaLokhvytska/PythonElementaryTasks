import os

result = set()
for root, dirs, files in os.walk("./main"):
    for file in files:
        if file.endswith(".py"):
            path = root.replace('\\', '/')[2:]
            result.add(path)

path_list = list(result)
path_list.sort()
for el in path_list:
    print(el)
