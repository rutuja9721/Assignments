#Read json file and print all lines, search specific tags

import json

file1 = open("D:\PythonWork\PythonWork\json2.json")

data = json.load(file1)

print(data)

# for key,value in data.items():
#     print(key , " : " , value)
#
# print()
#
# for i in data:
#     print(i)
#
# print()
#
# print(data['quiz'].get('maths'))

def get_key(data, lookup):
    for k,v in data.items():
        if (k == lookup):
            if (type(v) is dict):
                print(k, " is dictionary here")
            print(data[k])
        if(type(v) is dict):
            get_key(v,lookup)

get_key(data, 'viewer rating')
