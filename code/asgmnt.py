import cv2
import numpy as np

img1 = cv2.imread('n4.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('ovrly.jpg', cv2.IMREAD_COLOR)

rows,cols,channels = img2.shape

roi = img1[0:rows,0:cols]

#cv2.imshow("roi",roi)

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2gray",img2gray)

mask_gry = cv2.bitwise_not(img2gray)

#cv2.imshow("mask_gry",mask_gry)

#mask1 = cv2.bitwise_not(img2)

#cv2.imshow("mask1",mask1)


ret,mask = cv2.threshold(img2gray, 20, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("mask",mask)

print ("return")
print(ret)

img_fg = cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow("img_fg",img_fg)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv",mask_inv)

img_roi = cv2.add(img_fg,img2)
cv2.imshow("img_roi",img_roi)


img1[0:rows,0:cols] = img_roi
cv2.imshow("img1",img1)



#cv2.imshow("img2gray",img2gray)
#cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
