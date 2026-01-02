# CLAHE (Contrast Limited Adaptive Histogram Equalization).
# Create a CLASH object (Arguments are optional)
# it is used to enhance image and also handle noise from image.
# gray scale img is required.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(400,200))

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(img_gray)
cv2.imshow('clahe',cl1)

hist2=cv2.calcHist([cl1],[0],None,[256],[0,256])
plt.plot(hist2)
plt.title("CLAHE")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()