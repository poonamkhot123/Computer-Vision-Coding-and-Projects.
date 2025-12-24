# Morphological trasnformations.
""" Morphological transfomrmations are some simple operations based on the image shape.
   it is normally perform on binary image.
   it needs two inputs - 1) - original image
                        2) - strcturing element(kernel).
   Two basics Morphological transformationsare 1) Erosion and 2) Dilation."""


import cv2
import numpy as np

img = cv2.imread("plastic-color-balls.jpg",0)
img = cv2.resize(img,(600,400))
_, mask = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8) # 5x5 kernel with full of ones.
e = cv2.erode(mask,kernel)


cv2.imshow("img",img)
cv2.imshow("mask==",kernel)
cv2.imshow("mask==",mask)
cv2.imshow("erosion==",e)


# Dilation.
"""
It is just opposite of erosion.
here,a pixel element is '1' if atleast one pixel under the kernel is "1".
so it inc. the white region noise removal,erosion is followed by dilation.
Beacuase ,erosion removes white moises,but it also shrinks our object.
"""

kernel = np.ones((1,1),np.uint8)  # 5x5 kernel full of ones.
d = cv2.dilate(mask,kernel)  # iterations = 2 (optional paramerters) iterations.
cv2.imshow("dialate==",d)

# if you want then plot it.
from matplotlib import pyplot as plt
titles = ["img","mask","erosion","dilation"]
images= [img,mask,e,d]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([ ]),plt.yticks([])
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()