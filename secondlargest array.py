#program to find sencond largest number in array
arr=[10,20,30,40,50]
print("second largest number is:",arr[-2])
#program ti find even and odd in array
arr=[1,2,3,4,5]
evennumber=0
oddnumber=0
for i in arr:
    if i%2==0:
        evennumber +=1
    else:
        oddnumber +=1
print("even number in given array:",evennumber)
print("odd number in given array:",oddnumber)

