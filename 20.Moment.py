# Contours and its functions.....
"""
Moment
Approximation
ConvexHull
"""
import cv2
import numpy as np

img = cv2.imread("chota bhim image.jpg")
img = cv2.resize(img,(600,500))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,140,255,cv2.THRESH_BINARY_INV)

# findcountour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("Heirarchy==\n",hier)

for c in cnts:
    M = cv2.moments(c)
    print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

   # draw the contour and center of the shape on the image.
    cv2.drawContours(img,[c],-1,(0,255,0),2)
    cv2.circle(img,(cX,cY),7,(255,255,255),-1)
    cv2.circle(img,(cX,cY),7,(255,255,255),-1)
    cv2.putText(img,"center",(cX-20,cY -20),cv2.FONT_HERSHEY_COMPLEX,0.5,
                (255,255,255),2)




cv2.imshow("Original==",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

