import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        cv2.imshow("Camera Window", frame)

        mask = np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])
        dst = cv2.filter2D(frame, -1, mask)
        cv2.imshow("Sharpning", dst)
        key = cv2.waitKey(10) & 0xFF
        if (key == 27):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()