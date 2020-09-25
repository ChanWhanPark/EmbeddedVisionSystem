import cv2

img_basic = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR) # 이미지를 읽어들임
if img_basic is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

cv2.imshow('Image Basic', img_basic) # 이미지 출력
cv2.waitKey(0)

cv2.imwrite('result1.png', img_basic) # 이미지 파일 저장

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) # 흑백 사진으로 바꿈
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)

cv2.imwrite('result2.png', img_gray)
cv2.destroyAllWindows()