import Assignment28

def main():
    o1 = Assignment28.Engineer("A", "B", 23, "C", "D")
    o2 = Assignment28.Person("C", "B", 23, "C")

    o3 = [o1,o2]

    for i in o3:
        print(i.first_name)
        i.calculateTax()

    # o1.calculateTax()
    # print(o1.first_name)
    #
    # o2.calculateTax()
    # print(o2.first_name)

if __name__=="__main__":
    main()
else:
    print("Imported")