import cv2 as cv
import numpy as np

table = np.zeros((256), np.uint8)
for j in range(256):
    table[j] = int(j / 32) * 32

img = cv.imread("lenna.jpg", cv.IMREAD_GRAYSCALE)

imgGrayScale = cv.LUT(img, table)
cv.imshow("img", img)
cv.imshow("img_GrayScale", imgGrayScale)

cv.waitKey(0)