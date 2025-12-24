# Adaptive thresholding
# we use it beacuase simple thresholding not able to handle.
#different type of low luminous pixels.
# this , algorithm calculate the threshold for a small regions of the image.
# so we get multiple threshold for diff. regions in same image.

# Adaptive Method - It decides how thresholding value is calculated.
# cv2.ADAPTIVE_THRESH_MEAN_C:
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C:

# thrrshold(img,pixel_thresh,max_thresh_pixel,method,style,no._of_pixel,contact_mean)

import cv2
import numpy as np

img = cv2.imread("doremon.jpg",0)
img = cv2.resize(img,(400,400))
_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # simple

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Original image",img)
cv2.imshow("THRESH_BINARY",th1)
cv2.imshow("Adaptive thresh",th2)
cv2.imshow("Guassian img",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()