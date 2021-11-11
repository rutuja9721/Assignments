#Ask the user to pick any number between 0 and 100.
#Implement a guessing game program to identify the number picked up by user.
#(Use while loop)

number = int(input("Enter any number between 0 and 100"))

low = 0
high =100
mid=0

while(mid!=number):

    mid = (low+high)//2
    print("\nmid=" + str(mid))

    if(mid<number):
        low=mid+1

    if(mid>number):
        high=mid-1

print("\nYour number is : " + str(mid))