import cv2
import numpy as np

height = 20
width = 22
my_img = np.zeros((height, width), np.uint8)

f = open('image.txt', 'r')
for y in range(height):
    line = f.readline()
    print(line)
    for x in range(width):
        add = 4 * x
        my_img[y, x] = line[0 + add:4 + add]

f.close()
cv2.imshow("my_img", my_img)
cv2.waitKey(0)