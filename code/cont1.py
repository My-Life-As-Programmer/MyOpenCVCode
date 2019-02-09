import cv2
import numpy as np


img = cv2.imread('corner.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th_img , contours , hierarchy = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

print (len(contours))
cv2.drawContours(img,contours,0,(0,0,255),6)

cv2.imshow("img",img)
#cv2.imshow("gray",gray)
#cv2.imshow("threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()



