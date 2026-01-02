# half line probability method.
import cv2
import numpy as np


# second type of Hough Transformation.
img = cv2.imread("doremon.jpg")
img = cv2.resize(img,(400,200))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,20,250)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,
                       maxLineGap=50)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(100,200,125),2)


cv2.imshow("edges",edges)
cv2.imshow("lines",img)

cv2.waitKey(0)
cv2.destroyAllWindows()