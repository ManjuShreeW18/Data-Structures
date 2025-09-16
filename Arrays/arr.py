import array as arr
a=arr.array('I',[8,9,7,76,8])
print(a)
 
a.append(87)
a.extend([33,1]) #it adds these values
a.pop(3) #here we need to give index to rwmove the element
print(a)


arr=[1,2,3,4,5]
print(arr[0])
print(arr[1])
print(arr[-1])

arr.append(21)
print(arr)

arr.insert(2,10)
print(arr)

arr.remove(1)
print(arr)

print(arr.pop(-1))

arr2=[
    [2,3,4],
    [4,5,6],
    [7,8,9]
]
print(arr2)
print(arr2[0][2]) #accessing
print(arr2[1])

#multidimensional array

arr3=[
    [[1,2],[3,4]],  #table 1
    [[4,5],[7,8]],  #table 2
]

print(arr3)
print(arr3[0][1][1])

#traversal
l1=[32,45,6,7,8,99]
for i in range(len(l1)):
    print(l1[i])
  
    #   or

for i in l1:
    print(i)

print("reverse traversal ")
for i in l1[::-1]:  #reverse
    print(i)



