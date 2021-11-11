#Read the file category data and write all the lines containing category = "C1" to another file

file1 = open("D:\PythonWork\PythonWork\Data\catdata.txt","r")

file2 = open("D:\Python\Examplefile.txt","w")

lines = file1.readlines()

for line in lines:
    if("C1" in line):
        file2.write(line)
