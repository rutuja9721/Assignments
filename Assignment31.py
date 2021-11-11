#Use 24 to build employee-manager tree and findout hierarchy for any given employee.
#For example if user gives "Pranav" as input, findout all managers of Pranav till top boss.
#Sample output: Pranav ==> Mandar ==> Soham ==> Ishan ==> Swati ==> Saurabh

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

id = int(input("Enter id of an employee "))

if(id in empdict.keys()):
    emp_obj = empdict[id]
    if(id == root):
        print("The employee is the head")
        print("Name : " + emp_obj.name)
        manager_obj = emp_obj
    else:
        manager_obj = empdict[emp_obj.manager_id]
        print("Employee : " + emp_obj.name + " ==>" , manager_obj.name, end=" ")
    while(manager_obj.manager_id > 0 and id!=root):
        manager_obj = empdict[manager_obj.manager_id]
        print("==>", manager_obj.name, end=" ")

else:
    print("Id does not exist")
