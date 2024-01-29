#Write a  program to print even number between 10 and 20 using while

num = int(input("Enter the Min Value : "))
number = int(input("Enter the Max Value : "))
while num <= number:
    if(num % 2 == 0):
        print(num)
    num = num + 1