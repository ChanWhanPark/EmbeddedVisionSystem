import cv2 as cv

img = cv.imread('Lenna.jpg', cv.IMREAD_COLOR)
if img is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

res1 = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation=cv.INTER_CUBIC)
height, width = img.shape[:2]
res2 = cv.resize(img, (height*2, width*2), interpolation=cv.INTER_CUBIC)

cv.imshow("img", img)
cv.imshow("res1", res1)
cv.imshow("res2", res2)
cv.waitKey(0)

# 7주차 2_와 동일