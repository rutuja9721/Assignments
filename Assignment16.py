#Two-number sum : input list l1 = [2,18,11,23,34,3,22]
#Write a program to find out two numbers that have a sum = 45

l1 = [2, 18, 11, 23, 34, 3, 22]
l2 = []

for i in l1:
    for j in l1:
        if i != j:
            lsum = i + j
            if lsum == 45:
                l2.append([i, j])

res = list(set(tuple(sorted(k)) for k in l2))

# res1 = tuple((sorted(k))) for k in l2
#
# res2 = list(set(res1))
#
# print(res2)

print("List of numbers whose addition is 45 : " )
print(res)
