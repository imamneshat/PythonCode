# def avrage(a=9, b=2):
#     print("This is avrage is ", (a+b)/2)

# avrage(b=9)


# def name(fname, mname= "uuii", lname= "potter"):
#     print("hii", fname, mname, lname)

# name("UIUI", "QRTWY", "ppopoo")

def avrage(*numbers):
    sum= 0
    for i in numbers:
        sum = sum + i
    
    print("Avrage number is-->", sum / len(numbers))


avrage(5, 15, 8, 6)