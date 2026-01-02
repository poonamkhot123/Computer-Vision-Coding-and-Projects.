# Gray Scale Image Histogram.

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(400,200))

# Gray scale.
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])

plt.plot(hist)
plt.title("Gray Image.")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()