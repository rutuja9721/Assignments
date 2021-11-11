#Build a small application to query json file

import json
import pandas as pd
# from flatten_json import flatten

pd.set_option('display.max_columns', None)

file1 = open("D:\PythonWork\PythonWork\json2.json")

data1 = pd.read_json("D:\PythonWork\PythonWork\json2.json")

data = json.load(file1)

r = [{'quiz':a, q:q, **v, 'summary':data['summary'], 'viewer rating':data['viewer rating']}
          for a, b in data['quiz'].items() for q, v in b.items()]

print(r)

df = pd.DataFrame(r)

print(df)

# print(pd.concat({key:pd.DataFrame.from_dict(data[key], orient='index') for key in data.keys()}))

# print(data)

# print(pd.json_normalize(data, max_level=2))

# print(data1)
# df1 = pd.DataFrame(data)
#
# data2 = flatten(data)
#
# print(data2)

# print(df1)
#
# df = pd.json_normalize(data, record_path=['quiz'])
#
# print(df.head())
