# Extracting object from the image and place on another image.
# Random figure ROI orBackground sutraction.

import cv2
import numpy as np

# load two images
img1 = cv2.imread("chota bhim image.jpg")
img2 = cv2.imread("doremon.jpg")

img1 =cv2.resize(img1,(600,400))
img2 = cv2.resize(img2,(500,400))

# I want to fix image 2 data into img1.
row,column,channel = img2.shape
print(row,column,channel)

# roi ==
roi = img1[0:row,0:column]

# Now creating mask for img2
img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# create mask using threshold.
_, mask = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)

# remove bg
mask_inv = cv2.bitwise_not(mask)

# put mask into ROI
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)


# Take only region of figure from original image.
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)


# put img in ROI  and modify the main image.
result = cv2.add(img1_bg,img2_fg)

# cv2.imshow("bhim",img1)
# cv2.imshow("Doremon",img2)
# cv2.imshow("roi==",roi)

cv2.imshow("step -1 geay",img_gray)
cv2.imshow("strp -2 Mask==",mask)
cv2.imshow("step -3 Mask_inv",mask_inv)
cv2.imshow("step -4 mask_bg",img1_bg)
cv2.imshow("Step -5 mask fg",img2_fg)
cv2.imshow("Step-6",result)

final = img1
final[0:row,0:column] = result # final output.
cv2.imshow("step -7 == Final",final)


cv2.waitKey(0)
cv2.destroyAllWindows()