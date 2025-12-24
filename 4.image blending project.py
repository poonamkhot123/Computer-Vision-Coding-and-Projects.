# project on image blending using trackbars.

import cv2
import numpy as np

img1 = cv2.imread("chota bhim image.jpg")
img1 = cv2.resize(img1,(600,400))

img2 = cv2.imread("doremon.jpg")
img2 = cv2.resize(img2,(600,400))

# cv2.imshow("chota bhim==",img1)
# cv2.imshow("Doremon",img2)


def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)

# create track bar windows.
cv2.namedWindow("win")      
cv2.createTrackbar("alpha","win",1,100,blend)

# creating switch
switch = "0:OFF \n 1: ON"

#create track bar for switch
cv2.createTrackbar(switch,"win",0,1,blend)

while True:
    s = cv2.getTrackbarPos(switch,"win")
    a = cv2.getTrackbarPos("alpha","win")
    n = float(a/100)
    print(n)

    if s== 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow("dst",dst)
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()