#Ask the user to enter 10 numbers
#Store them in a list and print the list,
#find maximum in the list and print the maximum number

a = []

print("Enter a list of 10 elements")

for i in range(10):
    ele =int(input())
    a.append(ele)

max = a[0]

for i in range(1,len(a)):
    if(max<a[i]):
        max = a[i]

print("The maximum number is : " + str(max))