

# Function to insert an element at the beginning of an array
def Insert_Beg(arr,element):
     n=len(arr)
     new_arr=[0]*(n+1)
     for i in range(n):
        new_arr[i+1]=arr[i]
     new_arr[0]=element
     return new_arr
 
arr=[2,3,1,45,5]
element=54
print("Before insertiom:")
for i in range(len(arr)):
     print(arr[i],end=" ")
updated_arr=Insert_Beg(arr,element)
print("\nAfter insertion: ")
for i in updated_arr:
    print(i,end=" ")