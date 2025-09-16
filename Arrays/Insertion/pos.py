# Python program to insert given element at a given position
 
def Insert_Pos(arr,pos,element):
    n=len(arr)
    new_arr=[0]*(n+1)
 
    for i in range(pos):
        new_arr[i]=arr[i]
    new_arr[pos]=element
 
    for i in range(pos,n):
        new_arr[i+1]=arr[i]
    return new_arr
arr = [10, 20, 30, 40]
pos = 2
element = 50
 
updated_arr = Insert_Pos(arr, pos, element)
 
print("After insertion at a specific position:")
for i in updated_arr:
    print(i, end=" ")