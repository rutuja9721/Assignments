#Start with a hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99]
#Find the maximum number in this list (without using python readymade function)

a = [12,3,34,45,88,23,45,63,3,4,69,99]

max = a[0]

for i in range(1,len(a)):
    if(max<a[i]):
        max = a[i]

print("The maximum number is : " + str(max))