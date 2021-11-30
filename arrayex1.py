import array
arr= array.array('i',[1,2,3,4])
print(arr)
print(type(arr))

arr_1= array.array('f',[1.2,3.5,6.5,25,45,54])
print(arr_1[2])
arr_1.pop()
print(arr_1)