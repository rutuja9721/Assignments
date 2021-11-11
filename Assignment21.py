#Move elements to the last.
#Input l1:[2,3,5,6,7,2,4,2,6,2,3,9,7] and number given is 2
#Move all instances of 2 to the end of the list ==>
#l1:[3,4,5,6,7,4,6,3,9,7,2,2,2,2]

l1 = [2,3,5,6,7,2,4,2,6,2,3,9,7]

for i in l1:
    if(i == 2):
        l1.remove(i)
        l1.append(i)

print(l1)