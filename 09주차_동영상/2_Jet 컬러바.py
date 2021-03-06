import cv2 as cv
import numpy as np

table = np.zeros((50, 256, 3), np.uint8)

for i in range(50):
    for j in range(256):
        if j < 128:
            table[i, j, 0] = 255 - (j*2)
            table[i, j, 1] = j * 2
        else:
            table[i, j, 1] = 255 - (j*2)
            table[i, j, 2] = j * 2

cv.imshow("table", table)
cv.waitKey(0)