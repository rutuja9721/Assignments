#Get 3 numbers from the user and find the maximum number

x = input("Enter the first number ")
y = input("Enter the second number ")
z = input("Enter the third number ")

if(x>y) :
    if(x>z):
        print(x + " is the largest number")
    else :
        print(z + " is the largest number")
else:
    if(y>z):
        print(y + " is the largest number")
    else:
        print(z + " is the largest number")