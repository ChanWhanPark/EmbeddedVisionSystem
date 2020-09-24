import numpy as np

arr = np.array([10, 20, 30])

print(arr.size) # 배열의 크기
print(arr.dtype) # 배열 타입

for i in range(3):
    print(arr[i]) # 배열 요소별 호출

# 다양한 초기화 방법들
arr1 = np.arange(4)
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 2))
arr4 = np.random.randint(1, 6, (3, 3))

print(arr1)
print(arr2)
print(arr3)
print(arr4)