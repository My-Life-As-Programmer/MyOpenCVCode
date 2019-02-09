import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")
#							        th_val  max_val
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) 
# cv2.threshold(img, 12) -any thing above 12 is 1 whichs is white , below 12 is 0 whch is black

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY) 

gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3,otsu = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("final",img)
cv2.imshow("threshold",threshold)
cv2.imshow("threshold2",threshold2)
cv2.imshow("gaus",gaus)
cv2.imshow("otsu",otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()