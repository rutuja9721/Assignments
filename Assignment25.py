#Read employee manager file (create class and functions OOP)
#Store object in list and browse over list to print the objects

class empManager:

    def read_lines(self):
        file1 = open("D:\PythonWork\PythonWork\Data\empManager.txt", "r")
        lines = file1.readlines()
        return lines

o1 = empManager()
l1 = []
l1 = o1.read_lines()

print(l1)
