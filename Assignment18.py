#Find smallest difference between two numbers from two lists
#(one number from each list).
#Input l1: [2,4,6,8], l2:[3,10,18,19]. Output is 1 for this example

l1 = []
l2 = []

print("Enter 5 numbers in list 1 : ")
for i in range(5):
    l1.append(int(input()))

print("Enter 5 numbers in list 2 : ")
for i in range(5):
    l2.append(int(input()))

diff1 = 10000

for i in l1:
    for j in l2:
        diff = abs(i-j)
        if(diff<diff1):
            diff1 = diff

print("Minimum difference in the 2 lists is " + str(diff1))
