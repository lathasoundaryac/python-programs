a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
if a==b:
    print("Numbers are Equal")
else:
    print("Numbers are not Equal")
if a < b:
    print("A is Greater than B")
else:
    print("B is Greater than A")
if a > b:
    print("A is Smaller than B")
else:
    print("B is Smaller than A")
if a <= b:
    print("A is greaterthan equal to B")
else:
    print("B is greaterthan equal to A")
if a >= b:
    print("A is Smallerthan equal to B")
else:
    print("B is Smallerthan equal to A")
smallest =min(a,b)
print("smallest number:",smallest)
greater =max(a,b)
print("greater number:",greater)

