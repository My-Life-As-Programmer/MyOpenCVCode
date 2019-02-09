import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("me.jpg",cv2.IMREAD_GRAYSCALE)
# cv2.imshow("chaitu", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("chaitu.jpg",img)

plt.imshow(img,cmap="gray")
plt.show()



