#Read file category data and print lines containing category = "C1"

file1 = open("D:\PythonWork\PythonWork\Data\catdata.txt","r")

lines = file1.readlines()

for line in lines:
    if("C1" in line):
        print(line)
