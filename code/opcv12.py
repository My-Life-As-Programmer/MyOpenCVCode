import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('me.jpg', 1)
mask = np.zeros(img.shape[:2],np.uint8)
cv2.imshow('original',img)
bgm = np.zeros((1,65))
fgm = np.zeros((1,65))

rect = (60,60,400,400)

cv2.grabCut(img,mask,rect,bgm,fgm,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype("uint8")
img = img*mask2[:,:,np.newaxis]


plt.imshow(img)
plt.colorbar()
plt.show()


cv2.imshow('Detected',img)
#cv2.waitKey(0)