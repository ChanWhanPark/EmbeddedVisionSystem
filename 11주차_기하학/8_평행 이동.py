import cv2
import numpy as np

img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 50]])
# 변환행렬은 2 x 3의 2차원 행렬임
# [1, 0, x축 이동], [0, 1, y축 이동]의 형태

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()