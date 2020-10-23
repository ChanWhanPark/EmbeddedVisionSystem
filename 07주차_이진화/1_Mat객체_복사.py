import copy
import numpy as np

a = [1, 2, 3]
b = a
print(id(a), '주소만 복사')

b[0] = 6
print(id(b), b, a) # b 변경 시 주소 변경
b = [1, 2]
print(id(b))

b = copy.deepcopy(a)
print(id(a), '다른 메모리 주소에 데이터를 복사')
b[0] = 7
print(id(b), b, a)

c = np.zeros((10, 20), np.uint8)

print(id(c), 'c 주소를 출력')
d = c
print(id(d), 'd 주소를 출력')
e = c.copy()
print(id(e), 'e 주소를 출력')