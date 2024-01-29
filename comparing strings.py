a="ABC"
b="ABC"
print(a==b)
print(a!=b)

#startwith endwith
string="latha soundarya"
print(string.startswith("tha"))
print(string.endswith("arya"))

#trimming string with strip and split
print(string.strip("soundarya"))
stripstring="hello world"
print(stripstring.split(" "))

#converting int to string
num=10
num1=str(num)
print(num1)
print(type(num1))

#converting upper to lower case
str1="hello"
str2="World"
print(str1.upper()+" "+str2.lower())
