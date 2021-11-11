#Write a function to compare two lists and find out if the two lists are same.

a = []
b = []

print("Enter a list of 5 numbers")

for i in range(5):
    ele = int(input())
    a.append(ele)

a.sort()

print("Enter a second list of 5 numbers")

for i in range(5):
    ele = int(input())
    b.append(ele)

b.sort()

flag = 0

for i in range(5):
    if(a[i] != b[i]):
        flag = 1
        break

if(flag == 0):
    print("Lists are same")
else:
    print("Lists are not same")