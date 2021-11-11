#Find duplicate lines in file

file1 = open("D:\PythonWork\PythonWork\Data\countrydata.txt","r")

seen = set()

for line in file1:
    lower = line.lower()
    if(lower in seen):
        print(line)
    else:
        seen.add(lower)





