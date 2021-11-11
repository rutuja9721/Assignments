#Three number sum: input list l1 = [2,18,11,23,34,3,22]
#Write a program to find out three numbers that have sum = 43

l1 = [2,18,11,23,34,3,22]

l2 = []

for i in l1:
    for j in l1:
        sum = 0
        if(i!=j):
            sum = i + j
            for k in l1:
                if(i!=k | j!=k):
                    sum1 = sum
                    sum1 = sum1 + k
                    if(sum1 == 43):
                        l3 = [i,j,k]
                        l2.append(l3)

res = list(set(tuple(sorted(k)) for k in l2))

print("List of numbers whose addition is 43 : " )
print(res)


