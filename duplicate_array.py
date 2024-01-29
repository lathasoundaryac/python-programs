#Write a function to find the duplicate values of an array
import numpy as np
list_1=[10,20,30,10,50,30]
length_list_1=len(list_1)
dup=[]
for i in range(length_list_1):
    k=i+1
    for j in range(k,length_list_1):
        if list_1[i]==list_1[j]and list_1[i] not in dup:
            dup.append(list_1[i])
print("Duplicate values:",dup)
##Write a method to remove duplicate elements from an array
print("non-duplicate values are:",np.unique(list_1))