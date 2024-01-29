#Write a program to palindrome or not.
num = int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    value=num%10
    rev=rev*10+value
    num=num//10
if temp==rev:
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")
#program to check even or odd
a=int(input("enter a number:"))
if(a%2==0):
    print("{0} is even".format(a))
else:
    print("{0} is odd".format(a))