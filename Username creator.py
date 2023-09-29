import sys
a = input("Name: ")
b = input("Surname: ")

# in text file
with open ('write1.txt', 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    
    print("Dear Colleagues,\n\nCompleted!\n")

    print('User: '+ a,b)

    a = a.lower()
    b = b.lower()
    print(("Username: ")+a[0]+(".")+b)

    c = a[0]+(".")+b

    print("E-Mail:"+c+("@yourmaildomain"))

    print("Password: Standart password ")

#terminal
    sys.stdout = original_stdout
    print("Dear Colleagues,\n\nCompleted!\n")

    print('User: '+ a,b)

    a = a.lower()
    b = b.lower()
    print(("Username: ")+a[0]+(".")+b)

    c = a[0]+(".")+b

    print("E-Mail:"+c+("@yourmaildomain"))

    print("Password: Standart password ")
