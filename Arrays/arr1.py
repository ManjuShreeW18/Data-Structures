from array import *
vals=array('i',[3,6,4,-2,6]) #'i' specifies that it is a signed int
print(vals)
print(vals.typecode) #gives the type
print(vals.buffer_info()) #gives the size and address
print(vals[2]) #to print the element using index
vals.append(54)
vals.remove(3)
 
# to print all the numbers
print("Here are all the elements")
for i in vals:
    print(i)