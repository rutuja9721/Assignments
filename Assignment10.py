#Ask the user to enter user_id and user_name for 10 users.
#Store them in a dictionary using user_id as key and name as value.
#Search for user_id = 10

data = {}

for i in range(3):
    key = int(input("Enter the user_id : "))
    value = input("Enter the user_name : ")
    data[key] = value

print(data)

key = 10

if key in data.keys():
    print("User_id found")
    print("Name : " + data[key])
else:
    print("Not found")
