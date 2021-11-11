#Write a function to get maximum element of list and second highest element in a list

a = []

print("Enter a list of 5 elements")

for i in range(5):
    ele = int(input())
    a.append(ele)

max = a[0]

for i in range(1,len(a)):
    if(max<a[i]):
        max = a[i]

if(a[0] == max):
    max2 = a[1]
    for i in range(2, len(a) - 1):
        if (max2 < a[i]):
            max2 = a[i]

else:
    max2 = a[0]
    for i in range(1, len(a) - 1):
        if (a[i] == max):
            continue
        if (max2 < a[i]):
            max2 = a[i]

print("The maximum number is : " + str(max))
print("The second highest number is : " + str(max2))