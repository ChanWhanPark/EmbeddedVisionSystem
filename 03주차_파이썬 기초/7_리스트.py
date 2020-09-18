x = [3, 2, 1]
y = ["리스트", "문자열"]
z = [1, 2, 2.2, "리스트"]

print(x)
print(y)
print(z)
print(x+y)

numLen = len(x)
sorList = sorted(x)
sumList = sum(x)

print(numLen)
print(sorList)
print(sumList)

for i in z:
    print(i)

print(y.index("문자열"))
print("리스트" in y)