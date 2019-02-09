import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('output.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret,frame = cap.read()
	bg = fgbg.apply(frame)
	
	cv2.imshow("original",frame)
	cv2.imshow("bg",bg)
	fg = cv2.bitwise_and(frame,frame,mask=bg)
	cv2.imshow("fg",fg)
	
	gray = cv2.cvtColor(fg,cv2.COLOR_BGR2GRAY)
	#blur = cv2.GaussianBlur(fg,(15,15),0)
	#cv2.imshow("blur",blur)
	blur = cv2.bilateralFilter(fg,15,75,75)
	cv2.imshow("blur",blur)
	
	#final = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)
	#cv2.imshow("final",final)
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
	