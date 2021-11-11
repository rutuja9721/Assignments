#Read yaml file and print all lines, search specific tags

import yaml

file1 = open("D:\PythonWork\PythonWork\Data\categories.yaml")

data = yaml.safe_load(file1)

for i in data['sports']:
    print(i)