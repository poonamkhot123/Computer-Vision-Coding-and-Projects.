# Histogram equalization is good when of the image is confined
# to a particular region.
"""
It accept the gray scale image.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(400,200))

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img_gray)

res = np.hstack((img_gray,equ))
res = np.hstack((img_gray,equ)) #stacking images side-by-side.

cv2.imshow("equ",res)
hist1 = cv2.calcHist([equ],[0],None,[256],[0,256])

plt.plot(hist1)
plt.title("Equalization")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


