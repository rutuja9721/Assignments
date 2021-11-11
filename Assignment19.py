#Find out the largest range -
#Input: l1:[1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7]
#Hint sort list in ascending order.
#Only consider those parts that are consecutive

l1 = [1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7]

l1.sort()
print(l1)
l2 = []
i = 0

while i != (len(l1)-1):
    l3 = []
    if(l1[i] + 1 == l1[i+1]):
        l3 = [l1[i]]
    j=i
    while(l1[j+1] == l1[j] + 1):
        l3.append(l1[j+1])
        j+=1
    if(l3):
        l2.append(l3)
    i = j + 1

max = -1
k=-1

for index,list in enumerate(l2):
    if(len(list)>max):
        max = len(list)
        k=index

print("Longest range is : ", len(l2[k]), " -> ",l2[k])



