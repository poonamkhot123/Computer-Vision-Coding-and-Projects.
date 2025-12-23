# Create a function which help to find co-ordinate of any and its color.


import cv2
import numpy as np

def mouse_event(event,x,y,flg,param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flag==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN

    # for L-button
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)

        cord = "." + str(x) + "," +str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        #cv2.imshow("image",img)

    # for R-button
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        color_bgr = "." + str(b) + "," + str(g) + "," + str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
       # cv2.imshow("image",img)

cv2.namedWindow(winname="res")

img = np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",mouse_event)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()