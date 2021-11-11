#Build a small application to query yaml file

import yaml
import pandas as pd

file1 = open("D:\PythonWork\PythonWork\Data\yaml_dict.yaml")

data = yaml.safe_load(file1)

print(data)

print(pd.concat({key:pd.DataFrame.from_dict(data[key], orient='index') for key in data.keys()}))

