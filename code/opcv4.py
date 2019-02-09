import cv2
import numpy as np

img = cv2.imread('me.jpg', cv2.IMREAD_COLOR)

px = img[500,500]

print(px)

#for i in range(500):
#	img[i,i] = [i if i<255 else i-255, i if i<255 else i-255, i if i<255 else i-255]

#img[500,500] = [0, 255, 0]
#px = img[500,500]

#print(px)

cv2.imshow("image window", img)


roi = img[100:150 , 200:300] #= [255, 255, 255]

img[0:50, 0:100] = roi

cv2.imshow("image window", img)

cv2.waitKey(0)
cv2.destroyAllWindows()