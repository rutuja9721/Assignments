#Take a two dimensional array from user as matrix
#Implement zig-zag traverse ==> 1,2,4,7,5,3,6,8,10,11,9,12

matrix = []

rows = int(input("Enter number of rows "))

col = int(input("Enter number of columns "))

print("Enter the matrix")

for i in range(rows):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)

# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end=" ")
#     print()

final = [[] for i in range(rows+col-1)]

for i in range(rows):
    for j in range(col):
        sum = i+j
        if(sum%2 == 0):
            final[sum].insert(0, matrix[i][j])
        else:
            final[sum].append(matrix[i][j])

print(final)

