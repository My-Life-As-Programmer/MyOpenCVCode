import cv2
import numpy as np

img = cv2.imread('n4.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#kernel = np.ones((15,15),np.float32)
blur1 = cv2.GaussianBlur(gray,(15,15),0)
blur2 = cv2.GaussianBlur(gray,(15,15),10)
blur3 = cv2.GaussianBlur(gray,(15,15),15)
blur4 = cv2.GaussianBlur(gray,(15,15),20)
blur5 = cv2.GaussianBlur(gray,(15,15),25)

cv2.imshow("blur1",blur1)
cv2.imshow("blur2",blur2)
cv2.imshow("blur3",blur3)
cv2.imshow("blur4",blur4)
cv2.imshow("blur5",blur5)
cv2.imshow("original",gray)
cv2.waitKey(0)