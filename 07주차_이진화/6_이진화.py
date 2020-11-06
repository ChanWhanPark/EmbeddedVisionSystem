import cv2 as cv

img = cv.imread('Lenna.jpg', cv.IMREAD_GRAYSCALE)

ret, mask = cv.threshold(img, 128, 256, cv.THRESH_BINARY)
cv.imshow("Original Image", img);
cv.imshow("New Image", mask);

cv.waitKey(0)
cv.destroyAllWindows()