import win32api
import time
import cv2
import numpy as np



face_cscd = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cscd = cv2.CascadeClassifier("haarcascade_eye.xml")



cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cscd.detectMultiScale(gray)
	for (x,y,w,h) in faces:
		win32api.SetCursorPos((int(x+w/2),int(y+h/2)))
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		#cv2.imshow("video",frame)
		eyes = eye_cscd.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,255),2)
	cv2.imshow("video",frame)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()

'''
for i in range(500):
	x=y=i
	win32api.SetCursorPos((x,y))
	time.sleep(.02)
'''