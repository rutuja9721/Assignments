#Build a small application to use OS libraries to generate report on
#Directories, files and size of files on your computer (use os.walk)

import os
# print(os.name)
#
# print(os.environ['HOMEPATH'])
#
# print(os.getcwd())

s_path = r'C:\Users\dell\PycharmProjects'

for roots, dirs, files in os.walk(s_path):
    print("Root : " + roots)
    for dir in dirs:
        print("Dir : " + dir)
    for file in files:
        print("Files : " + file)
        fp = os.path.join(roots, file)
        # print(fp)
        # print(os.path.abspath(fp))
        print("Size : " , os.path.getsize(fp))
        # absp = os.path.abspath('r\'' + file)
        # print(absp)
        # print("size : " , os.path.getsize(absp))