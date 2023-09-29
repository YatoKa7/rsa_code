import sys
a = input("Name: ")
b = input("Surname: ")


with open ('write.txt', 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    
print("Dear Colleagues,\n\n Completed!")

print('User: '+ a,b)

a = a.lower()
b = b.lower()
print(("Username: ")+a[0]+(".")+b)

c = a[0]+(".")+b

print("E-Mail:"+c+("@yourmaildomain"))

print("Password: Standart password ")