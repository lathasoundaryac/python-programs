a=[1,2,3]
try:
    print("second element = ",a[1])

    print("fourth element=",a[3])

except:
    print("An error accurred")
print()

b=[3,2,1]
try:
    a==b
except:
    print("they are not equal")
else:
    print("Both Equal")
print()
try:
    k=5/0
    print(k)
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("This is always executed")
