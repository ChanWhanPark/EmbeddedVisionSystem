import cv2
import numpy as np

img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

center = (cols/2, rows/2) # 중심 좌표
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# 45도 돌리며 1배 Scale

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()