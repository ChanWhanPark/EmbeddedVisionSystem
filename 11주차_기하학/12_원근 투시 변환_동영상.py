import cv2
import numpy as np
cap = cv2.VideoCapture(0)
global point

point = []
point2 = np.float32([[10, 10], [10, 500], [500, 10], [500, 500]])

def mouse_callback(event, x, y, flags, param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN and count < 4:
        count = count + 1
        point.append([x, y])
        print(point)
        cv2.imshow("Camera Window", frame)

count = 0
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        cv2.imshow("Camera Window", frame)
        cv2.namedWindow('Camera Window')
        cv2.setMouseCallback('Camera Window', mouse_callback)
        for i in range(4):
            cv2.circle(frame, tuple(point[i]), 10, (255, 0, 0), -1)
        if (count >= 4):
            point1 = np.float32(point)
            M = cv2.getPerspectiveTransform(point1, point2)
            dst = cv2.warpPerspective(frame, M, (500, 500))
            cv2.imshow("New Window", dst)
        key = cv2.waitKey(10) & 0xFF # waitKey(10)에서는 영상이 멈춘다
        if (key == 27):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()