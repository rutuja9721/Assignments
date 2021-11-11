#Ask the user to enter name, age and address and let the user know if user can do voting

name = input("Enter your name ")
age = int(input("Enter your age "))
address = input("Enter your address ")

print("Name : " + name)
print("\nAge : " + str(age))
print("\nAddress : " + address)

if(age>=18):
    print("You can vote")
else:
    print("You are ineligible for voting")
