#Write a program to compute factorial of a number using recursive function

number = int(input("Enter a number"))

def calc_fact(number):
    if(number == 1):
        return number
    else:
        return number * calc_fact(number-1)

fact = 1
fact = calc_fact(number)

print("Factorial is : " + str(fact))