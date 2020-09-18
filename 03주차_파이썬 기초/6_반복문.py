for i in range(5):
    print(i)
    print("for 반복")

i = 0
while i < 5:
    print(i)
    print("while 반복")
    i += 1

i = 0
while True:
    print("break문 테스트")
    i += 1
    if i > 5:
        break

for i in range(5):
    print("continue문 테스트")
    continue
    print("여기는 출력 X")