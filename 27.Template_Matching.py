"""
It is a method for searching and finding the location of a template image in 
a larger image.openCV comes with a function cv2.matchTemplate() for this
purpose. It simply slides the template image over the input image
( as in 2D convolution) and compares the template and patch of input
image under the template image.
"""

import cv2
import  numpy as np

# target
img = cv2.imread("doremon.jpg")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# load template.
template = cv2.imread("Doremon crop image.png",0)
w,h = template.shape[::-1]

# template matching
# this method accept the parameter(img,template,method)
res = cv2.matchTemplate(grey_img,template,cv2.TM_CCORR_NORMED)

print("res==",res)

threshold = 0.897
loc = np.where(res>=threshold) # finding bright pixel.

for i in zip(*loc[::-1]):
    print("i==",i)
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    

img = cv2.resize(img,(400,300))
cv2.imshow("img",img)
res = cv2.resize(res,(400,300))
cv2.imshow("match temp==",res)
cv2.waitKey(0)
cv2.destroyAllWindows()