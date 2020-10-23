import cv2
import numpy as np # copyto()를 사용하기 위함
img = cv2.imread("Lenna.jpg")
logo = cv2.imread("opencv.png")

gray_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray_logo, 10, 255, cv2.THRESH_BINARY_INV)
# line 6. logo의 색을 그레이색으로 변경
# line 7. 그레이색으로 변경된 로고를 이진화한다.

logo_height, logo_width, _ = logo.shape

roi = img[0: logo_height, 0: logo_width]
# line 13. (0, 0)부터 logo의 크기만큼의 img를 지정한다.

roi_logo = cv2.add(logo, roi, mask=mask_inv)
# line 16. roi로 지정된 영역에 mask_inv를 붙인다.
# 결과적으로 (0, 0)부터 로고의 크기만큼 흑백 로고가 생긴다.
result = cv2.add(roi_logo, logo)
# line 19. roi_logo에 기존 logo를 붙여 색을 입힌다.
# 결과적으로 roi_logo 위에 색이 입혀진 logo가 생긴다.
img[0:logo_height, 0:logo_width] = result
# line 22. 배경에 logo의 크기만큼 배경위에 색있는 로고를 입힌 result를 붙인다.
# 또는 np.copyto(roi, result)를 사용하기도 한다.

cv2.imshow("result_background", img)
cv2.waitKey()