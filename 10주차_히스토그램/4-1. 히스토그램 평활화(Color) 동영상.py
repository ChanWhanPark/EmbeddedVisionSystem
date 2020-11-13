import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        cv2.imshow("Camera Window", frame)
        frame[:, :, 0] = cv2.equalizeHist(frame[:, :, 0])
        frame[:, :, 1] = cv2.equalizeHist(frame[:, :, 1])
        frame[:, :, 2] = cv2.equalizeHist(frame[:, :, 2])
        cv2.imshow("After Histogram", frame)
        key = cv2.waitKey(10) & 0xFF
        if (key == 27):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()