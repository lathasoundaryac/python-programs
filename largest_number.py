# Write a program to print largest number among three numbers.
a= int(input("enter A vlaue:"))
b= int(input("enter B vlaue:"))
c= int(input("enter C vlaue:"))
if (a>=b)and(a>=c):
    print("greater number is :",a)

else:
    if(b>c):
        print("greater number is :",b)
    else:
        print("greater number is :",c)