#Ask the user to enter name and surname and concatenate name and surname.
#Print name and surname in lower case if name starts with b
#else print name in title case

first_name = input("Enter your first name ")
last_name = input("Enter your surname ")

c = first_name + " " + last_name

if(c.startswith('b') | c.startswith('B')):
    print(c.lower())
else:
    print(c.upper())