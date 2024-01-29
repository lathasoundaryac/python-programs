#Write a function to remove a specific element from an array
import array as ar
data= ar.array("i",[2,3,4,5])
set_a = set(data)
print("data : ",set_a)
set_a.discard(3)
print("data after discard",set_a)