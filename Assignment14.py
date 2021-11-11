#Write a program to compute the factorial of a number using function

number = int(input("Enter a number "))

def calc_factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    print("Factorial of " + str(number) + " is : " + str(fact))

calc_factorial(number)
