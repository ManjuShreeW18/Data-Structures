#time complexity O(log n)

def Binary_search(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        
        elif target<arr[mid]:
            end=mid-1

        else:
            start=mid+1
    return -1

arr=[1,2,34,5,56,7,8,9]
target=int(input("enter num:"))

index=Binary_search(arr,target)

if index!=-1:
    print(f"{target } found at index {index}")

else:
    print(f"{target} not found")