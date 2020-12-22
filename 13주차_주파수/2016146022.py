import cv2

img_org = cv2.imread('test1.png', cv2.IMREAD_COLOR)

# 1) 명도가 50이하인 데이터를 모두 찾고 , 그 중심 좌표를 기준으로 크기가 20짜리 빨간색 원을 그려주세요.
img_hsv = cv2.cvtColor(img_org, cv2.COLOR_BGR2HSV) # 색상, 조도, 명도 순으로 데이터 변경
darkx = []
darky = []
h, s, v = cv2.split(img_hsv) # 색, 조도, 명도 분리

height, width = v.shape
for i in range(height):
    for j in range(width): # -> 방향으로 탐색
        if v[i, j] <= 50:
            darkx.append(i)
            darky.append(j)
print(darkx)
print(darky)
for i in range(len(darkx)):
    cv2.circle(img_org, (darkx[i], darky[i]), 20, (0, 0, 255), 3)

# 2) 녹색 색상이 250 이상인 데이터를 모두 찾고, 그 중심 좌표를 기준으로 크기가 20짜리 녹색 원을 그려주세요.
greenx = []
greeny = []
b, g, r = cv2.split(img_org) # B, G, R 화소 분리
heightg, widthg = g.shape
for i in range(heightg):
    for j in range(widthg): # -> 방향으로 탐색
        if g[i, j] >= 250:
            greenx.append(i)
            greeny.append(j)
print(greenx)
print(greeny)
for i in range(len(greenx)):
    cv2.circle(img_org, (greenx[i], greeny[i]), 20, (0, 255, 0), 3)
cv2.imshow("2016146022", img_org)
cv2.waitKey(0)