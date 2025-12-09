import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
print(arr[1:4])
print(arr[[0,2,4]])
print(arr[arr>30])

numbers = list(map(int,input("Enter element into the list: ").split()))
arr = np.array(numbers)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))

arr = np.arange(1,13)
new_arr_demo = np.arange(0,4)
print(new_arr_demo)
print(arr)
row = int(input("Enter number for rows: "))
col = int(input("Enter no of cols: "))
if row*col==arr.size:
    new_arr = arr.reshape(row,col)
print(new_arr)

    