# image blending with openCV
# here we use two important functions cv2.add(),cv2.addweight()
#blending means addition of two images.
# if you want to blend two images then both have same size

import cv2
import numpy as np

img1 = cv2.imread("chota bhim image.jpg")
img1 =cv2.resize(img1,(600,400))

img2 = cv2.imread("doremon.jpg")
img2=cv2.resize(img2,(600,400))


cv2.imshow("chota bim==",img1)
cv2.imshow("Doremon==",img2)


# recommended to use cv2.add
# result1 = cv2.add(img1,img2)
# cv2.imshow("result==",result1)

# sum of both the weight = w1+w2 = 1(max)
# function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)

result2 = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow("result==",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()