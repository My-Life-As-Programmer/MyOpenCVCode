import cv2
import numpy as np

img1 = cv2.imread('n4.png', cv2.IMREAD_COLOR)
#img2 = cv2.imread('n5.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('creative.jpg', cv2.IMREAD_COLOR)

#cv2.imshow("1",img1)
#cv2.imshow("2",img2)
#cv2.imshow("3",img3)

#add= img1 + img2
#add = cv2.add(img1,img2)

#weightedadd = cv2.addWeighted(img1, 0.6, img2 ,0.4,0)
#							  image1 60% , image2, 40%, gamma value

# add capture to n4 without background

rows,cols,channels = img2.shape
# to get all the rows(pixels) n cols(pixels) n shape of the image   
roi = img1[0:rows,0:cols]
cv2.imshow("roi",roi)
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2gray",img2gray)
# to convert to gray color
ret,mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# to set the thrshold of the colors in the image
# (source,threshold value, replacing value, binary ivert/something else)
cv2.imshow("mask",mask)

mask_inv = cv2.bitwise_not(mask)
# inverting binary image 0 -> 1, 1 -> 0 , so black becomes white , white becomes black 
cv2.imshow("mask_inv",mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
# does bitwise and with  roi and mask_inv , stores in roi
cv2.imshow("img1_bg",img1_bg)
img1_fg = cv2.bitwise_and(img2,img2,mask=mask)
# does bitwise and with  img2 and mask , stores in img2
cv2.imshow("img1_fg",img1_fg)

dst = cv2.add(img1_bg, img1_fg)
cv2.imshow("dst",dst)

img1[0:rows, 0:cols] = dst

cv2.imshow("final",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()