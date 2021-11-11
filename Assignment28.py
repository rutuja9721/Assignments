#Create a Person Class with attributes (first name, last name, age and gender)
#Make age private and gender protected attribute
#Implement one method in person class as calculate tax (just print "base class tax calculation")
#Create two child classes Doctor and Engineer.
#Doctor class has an additional attribute "speciality" and
#override calculate tax method in doctor class (print "profit and loss based tax")
#and Engineer has additional attribute "decipline"
#and override calculate tax method (print("salary based tax").
#Create a main file name it as "inheritanceAndPolymorphism.py"
#Create object of Doctor class and Engineer class add two obejcts to list
#Browse over the list and call calculate tax method to see polymorphism in action.

class Person:
    __age = None
    _gender  = None

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self._gender = gender
        self.__age = age

    def calculateTax(self):
        print("Base class Tax calculation")

class Doctor(Person):

    def __init__(self, first_name, last_name, age, gender, speciality):
        super().__init__(first_name,last_name,age,gender)
        self.speciality = speciality

    def calculateTax(self):
        print("Profit and loss based tax")

class Engineer(Person):

    def __init__(self, first_name, last_name, age, gender, discipline):
        super().__init__(first_name,last_name,age,gender)
        self.discipline = discipline

    def calculateTax(self):
        print("Salary based tax")

# if __name__ == "__main__":
#     print ("Assignment28 is being run directly")
# else:
#     print ("Assignment28 is being imported")