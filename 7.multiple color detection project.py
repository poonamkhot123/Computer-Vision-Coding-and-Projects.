# color detection with trackbars-------

import cv2
import numpy as np

frame = cv2.imread("plastic-color-balls.jpg")
frame = cv2.resize(frame,(600,400))

def nothing(x):
    pass
cv2.namedWindow("Color Adjustment")

cv2.createTrackbar("Lower_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustment",0,255,nothing)

cv2.createTrackbar("Upper_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustment",0,255,nothing)


while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower_H","Color Adjustment")
    lower_s = cv2.getTrackbarPos("Lower_S","Color Adjustment")
    lower_v = cv2.getTrackbarPos("Lower_V","Color Adjustment")
    
    upper_h = cv2.getTrackbarPos("Upper_H","Color Adjustment")
    upper_s = cv2.getTrackbarPos("Upper_S","Color Adjustment")
    upper_v = cv2.getTrackbarPos("Upper_V","Color Adjustment")

    lower_bound = np.array([lower_h,lower_s,lower_v])
    upper_bound = np.array([upper_h,upper_s,upper_v])

    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    # filter mask with image.
    result = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("original frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
