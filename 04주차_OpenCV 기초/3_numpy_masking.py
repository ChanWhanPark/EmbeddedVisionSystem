import numpy as np

arr1 = np.random.randint(1, 20, (5, 5))

print(arr1)
arr2 = arr1 < 10 # 조건에 만족하는 부분은 True, 아니면 False
print(arr2)
arr1[arr2] = 100 # 조건에 만족하는 부분을 100으로 바꿈
print(arr1)