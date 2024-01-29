#Write a program to find Armstrong number or not
Anum=int(input("Enter number:"))
n=int(input("power of number"))
sum=0
temp=Anum
while temp >0:
    value= temp%10
    sum =sum+value ** n
    temp =temp//10
if Anum==sum:
    print(Anum, "Anum in an Armstrong number")
else:
    print(Anum, "Anum is not Armstrong number")