import cv2 as cv

img = cv.imread('Lenna.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow("img_org", img)
cv.imshow("img", img + 100)
cv.imshow("img.add", cv.add(img, 100))
cv.imshow("img_re", 255-img)
cv.waitKey(0)