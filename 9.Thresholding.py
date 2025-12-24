# Thresholding = It is basic image processing technique used to convert a grayscle
# image into a binary image(black & white) by separating objects
# from the background.

# uses
# To highlight objects
# To help in edge detection ,contour detection , segmentation.
# To simplify images

# types: simple thresholding,Adaptive thresholding.
# simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)

import cv2
import numpy as np

img = cv2.imread("doremon.jpg",0)
img = cv2.resize(img,(600,400))
# img = cv2.imshow("image.jpg",img)

_, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC) 
_, th4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("1 - THRESH_BINARY",th1)
cv2.imshow("2 - THRESH_BINARY",th2)
cv2.imshow("3 - THRESH_BINARY",th3)
cv2.imshow("4 - Thresh_binary",th4)
cv2.imshow("5 - THRESH_BINARY",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()