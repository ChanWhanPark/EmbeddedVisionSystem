import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        cv2.imshow("Camera Window", frame)
        cap_canny = cv2.Canny(frame, 50, 150)
        cv2.imshow("Canny Edge", cap_canny)
        key = cv2.waitKey(10) & 0xFF
        if (key == 27):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()