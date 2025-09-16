# insertion at beginning using built in func
 
arr=[8,3,5,43]
print("Array before inserrtion")
for i in range(len(arr)):
    print(arr[i],end=" ")
 
print("\nInsertion at beginning")
arr.insert(0,25)
 
for i in range(len(arr)):
    print(arr[i],end=" ")