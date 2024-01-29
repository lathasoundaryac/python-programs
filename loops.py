# Write a program to print the odd and even numbers.
num= int(input("enter number:"))
for i in range(num+1):
    if i % 2 ==0:
        print("even numbers:",i)
    else:
        print("odd numbers:",i)
