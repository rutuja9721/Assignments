#Read employee manager file (create class and functions OOP)
#and store in tree (you can built tree using dictionary)

import employee as emp

file1 = open("D:\PythonWork\PythonWork\Data\empManager.txt","r")

empdict = {}
managerdict = {}
count = 1

for line in file1:
    emp_id, name, age, height, salary, manager_id = line.strip().split(",")
    if(emp_id == "id"):
        continue

    else:
        tempEmp = emp.Employee(int(emp_id), name, int(age), float(height), int(salary), int(manager_id))
        empdict[tempEmp.emp_id] = tempEmp
        if(tempEmp.manager_id<0):
            root = tempEmp.emp_id
            continue

        if(tempEmp.manager_id in managerdict):
            managerdict[tempEmp.manager_id].append(tempEmp)
        else:
            child_list = []
            child_list.append(tempEmp)
            managerdict[tempEmp.manager_id] = child_list

def get_level(node):
    if(node == root):
        return 0
    level = 1
    emp_obj = empdict[node]
    manager_obj = empdict[emp_obj.manager_id]
    while(manager_obj.manager_id > 0 ):
        level +=1
        manager_obj = empdict[manager_obj.manager_id]
    return level

def print_func(node):
    if node in managerdict.keys():
        pre = ""
    else:
        pre = "|_"
    spaces = str(" " * get_level(node)) + pre
    print(spaces, empdict[node].emp_id)
    if node in managerdict.keys():
        if managerdict[node]:
            for i in managerdict[node]:
                print_func(i.emp_id)

print_func(root)









