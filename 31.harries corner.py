# Harris Corner Detection.

"""
openCV has the function cv2.cornerHarris() for this purpose.
Its argument:
img - input image,it should be grayscale and float32 type.
blockSize - it is the size of neighbourhood considered for corner detection.
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.

"""

import numpy as np
import cv2
img = cv2.imread("Amazon logo.jpg")
cv2.imshow("img",img)

# gray conversion
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#detect corner
res = cv2.cornerHarris(gray,3,3,0.04)

res = cv2.dilate(res,None)
img[res > 0.01 * res.max()] = [0,0,255] # marked color.

cv2.imshow('dist',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
