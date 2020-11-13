import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        cv2.namedWindow("Camera")
        cv2.createTrackbar('K','Camera',1,20,nothing)

        while (1):
            if cv2.waitKey(1) & 0xFF == 27:
                break
            m = cv2.getTrackbarPos('K', 'Camera')

            if m == 0:
                m = 1

            mask = np.ones((m, m), np.float32) / (m * m)

            dst = cv2.filter2D(frame, -1, mask)
            cv2.imshow('Camera', dst)
    else:
        break

cap.release()
cv2.destroyAllWindows()