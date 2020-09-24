import numpy as np

arr = np.arange(10)
arr1 = arr[::2]
arr2 = arr[1::2]
arr3 = arr[::-1]
arr4 = arr[3::-1]
arr5 = arr[1:6:2]

print(arr)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
