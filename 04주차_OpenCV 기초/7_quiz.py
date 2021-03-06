import numpy as np
import cv2

# 마우스 이벤트 콜백 발생 시 함수 실행
def mouse_callback(event, x, y, flags, param):
    global keyflag
    if event == cv2.EVENT_LBUTTONDOWN:
        keyflag = True
        cv2.circle(img, (x, y), 10, (255, 255, 255), -1) # 도형함수
        print("키눌름")
    if event == cv2.EVENT_MOUSEMOVE:
        if keyflag == True:
            cv2.circle(img, (x, y), 10, (255, 255, 255), -1)  # 도형함수
            print("키움직임")
    if event == cv2.EVENT_LBUTTONUP:
        keyflag = False;
        cv2.circle(img, (x, y), 10, (255, 255, 255), -1)  # 도형함수
        print("키떨어짐")
img = np.zeros((512,512,3), np.uint8)
# 마우스 이벤트 콜백 받을 윈도우 창
cv2.namedWindow('image')

# image 원도우에서 마우스 이벤트가 발생하면 함수 호출
cv2.setMouseCallback('image', mouse_callback)

while(1): # 무한 루프로 돌면서 이미지에 변화 표현
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == 27: # esc로 종료
        break

cv2.destroyAllWindows()