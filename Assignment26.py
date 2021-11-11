#Define a class with List as an attribute of the class
#Create an instance of that class and try to implement shallow copy and deep copy

import copy

class Copy_Demo:

    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

o1 = Copy_Demo()

print(o1.old_list)
o2 = copy.copy(o1)
print(o2.old_list)
o3 = copy.deepcopy(o1)
print(o3.old_list)

o1.old_list.append([4, 4, 4])

print(o1.old_list)
print(o2.old_list)
print(o3.old_list)

o1.old_list[1][1] = 'AA'

print(o1.old_list)
print(o2.old_list)
print(o3.old_list)

#
# l1 = [1,2,3,4,5]
# l2 = copy.copy(l1)
#
# print(l1)
# print(id(l1[1]))
# print(l2)
# print(id(l2[1]))
#
# l1[1] = 10
#
# print(l1)
# print(id(l1[1]))
# print(l2)
# print(id(l2[1]))

