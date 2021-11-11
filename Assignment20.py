#Find out the longest peak -
#Input: l1:[3,23,25,4,5,8,2,5,6,7,9,11,3,1,0, 22,34]
#Length of largest peak in this problem is 9

l1= [3,23,25,4,5,8,2,5,6,7,9,11,3,1,0, 22,34]

#l1 = [1, 2, 3, 4, 5, 6, 8, 20, 21, 22, 23, 24, 25, 26, 33, 32, 71, 87]

print(l1)

valley = [0] * len(l1)

for i in range(len(l1)):
    if(i == 0):
        if(l1[i]<l1[i+1]):
            valley[i] += 1
            continue

    if(i == (len(l1)-1)):
        if (valley[i-1] != 1):
            valley[i] += 1
            continue

    if (l1[i] < l1[i-1] and l1[i]<l1[i+1]):
        valley[i] += 1

print(valley)

length = []

for i in range(len(valley)):
    count = 2
    if(i!=(len(valley)-1) and valley[i] ==1):
        j=i
        while valley[j+1]!=1:
            count += 1
            j += 1
        length.append(count)

print(length)

print("Largest peak is : " + str(max(length)))
