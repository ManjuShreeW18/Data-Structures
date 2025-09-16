def Linear_search(arr,value):
    for i in range(len(arr)):
        if (arr[i]==value):
            return i
    return -1
lst=[1,2,3,45,6]
find=45
ans=Linear_search(lst,find)
print(ans)