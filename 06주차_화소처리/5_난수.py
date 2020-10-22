import cv2
import numpy as np

width = 500
height = 500

image = np.ones((height, width, 3), dtype=np.uint8)
cv2.randn(image, (0, 0, 0), (255,255,255))

cv2.imshow("result", image)
cv2.waitKey(0)