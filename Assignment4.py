#Ask the user to enter a number.
#If the number is in 1s then print one,
#if number is in 10s then print ten,
#if number is in 100s then print hundred,
#if number is in 1000 print thousand.
#Try to implement this using if-elif-else as well as switch case

number = int(input("Enter a number up to 4 digits "))

print("\nEntered number is : " + str(number))
if(number//10 == 0):
    print("One")
elif(number//100 == 0):
    print("Ten")
elif(number//1000 == 0):
    print("Hundred")
elif(number//10000 == 0):
    print("Thousand")
else:
    print("Number greater than 10000")





