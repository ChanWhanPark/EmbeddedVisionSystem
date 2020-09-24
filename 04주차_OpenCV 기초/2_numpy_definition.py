import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1.reshape((2, 2))
print(arr2.shape)
print(arr2)

arr3 = np.arange(4).reshape(1, 4)
arr4 = np.arange(8).reshape(2, 4)
arr5 = np.concatenate([arr3, arr4], axis=0)
print(arr5.shape)
print(arr5)

arr6 = np.arange(8).reshape(2, 4)
left, right = np.split(arr6, [2], axis=1)
print(left.shape)
print(right.shape)
print(right)