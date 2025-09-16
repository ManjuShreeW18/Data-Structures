# Python program to insert a given element at the end
# without using built-in methods
 
def insert_at_end(arr, element):
    n = len(arr)
    new_arr = [0] * (n + 1)
    for i in range(n):
        new_arr[i] = arr[i]
    new_arr[n] = element #to insert at end we used 'n'
    return new_arr
 
arr = [10, 20, 30, 40]
element = 50
 
updated_arr = insert_at_end(arr, element)
 
print("After inserting at the end:")
for i in updated_arr:
    print(i, end=" ")