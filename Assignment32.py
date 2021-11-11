#Build employee-manager tree and findout nearest common manager for any two employees given by user.

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

id1 = int(input("Enter 1st id "))
id2 = int(input("Enter 2nd id "))

emp_obj1 = empdict[id1]
emp_obj2 = empdict[id2]

if(get_level(emp_obj1.emp_id) != get_level(emp_obj2.emp_id)):

    if(get_level(emp_obj1.emp_id) > get_level(emp_obj2.emp_id)):

        while(get_level(emp_obj1.emp_id) != get_level(emp_obj2.emp_id)):
            emp_obj1 = empdict[emp_obj1.manager_id]
    else:
        while (get_level(emp_obj1.emp_id) != get_level(emp_obj2.emp_id)):
            emp_obj2 = empdict[emp_obj2.manager_id]

man_obj1 = empdict[emp_obj1.manager_id]
man_obj2 = empdict[emp_obj2.manager_id]

while (man_obj1.emp_id != man_obj2.emp_id):
    man_obj1 = empdict[man_obj1.manager_id]
    man_obj2 = empdict[man_obj2.manager_id]

print("Nearest common manager is ", man_obj2.emp_id, " ==> Name : " , man_obj2.name)