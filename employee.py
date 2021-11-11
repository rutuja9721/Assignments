
class Employee:
    num_employee = 0

    def __init__(self, emp_id, name, age, height, salary, manager_id):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.height = height
        self.salary = salary
        self.manager_id = manager_id
        self.__class__.num_employee += 1

    def printEmp(self):
        print("Id : " , self.emp_id)
        print("Name : " , self.name)
        print("Age : ", self.age)
        print("Height : ", self.height)
        print("Salary : ", self.salary)
        print("Manager id : ", self.manager_id)
