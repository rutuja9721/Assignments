#Read employee manager file (create class and function OOP)
#Create Class Variable numEmployee and add its increment in constructor of the class

class EmpManager:
    count = 0
    def __init__(self):
        # self.__class__.count += 1
        type(self).count +=1

    def __del__(self):
        type(self).count -= 1

    def read_func(self):
        file1 = open("D:\PythonWork\PythonWork\Data\empManager.txt","r")
        lines = file1.readlines()
        print(lines)

# print(EmpManager)

e1 = EmpManager()
# print(e1)
# print(hex(id(EmpManager.count)))
print(EmpManager.count)
# e1.read_func()
e2 = EmpManager()
print(EmpManager.count)
# print(hex(id(EmpManager.count)))
# print(e2.count)
del e2
print(EmpManager.count)


# class C:
#     counter = 0
#
#     def __init__(self):
#         type(self).counter += 1
#
#     def __del__(self):
#         type(self).counter -= 1
#
#
# if __name__ == "__main__":
#     x = C()
#     print("Number of instances: : " + str(C.counter))
#     y = C()
#     print("Number of instances: : " + str(C.counter))
#     del x
#     print("Number of instances: : " + str(C.counter))
#     del y
#     print("Number of instances: : " + str(C.counter))