import cv2 as cv
import numpy as np

img1 = np.zeros((50, 256), np.uint8)
img2 = np.zeros((50, 256), np.uint8)

for i in range(50):
    for j in range(256):
        img1[i, j] = j
        img2[i, j] = int(j / 32) * 32

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.waitKey()