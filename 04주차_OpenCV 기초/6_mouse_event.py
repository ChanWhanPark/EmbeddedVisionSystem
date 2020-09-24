import numpy as np
import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1) # 도형함수
        print("키눌림")

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

cv2.setMouseCallback('image', mouse_callback)

while(1):
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()