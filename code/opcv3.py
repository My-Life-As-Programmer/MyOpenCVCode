import cv2
import numpy as np

img = cv2.imread('me.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (200,100), (0,255,255), 15)
cv2.rectangle(img,(10,20),(300,400),(0,0,255),10)
cv2.circle(img, (100,200), 45, (255,0,0), 10)

# polygon 
pts = np.array([[100,500],[200,300],[400,350],[100,300]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],False, (0,255,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"chaitu", (200,500), font, 1 , (0,0,255), 5 ,cv2.LINE_AA)

cv2.imshow("image window line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()