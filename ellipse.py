
import cv2

image = cv2.imread("Amazon logo.jpg")
# image = cv2.resize(image,(600,700))

#ellipse - accept(img,start,(length,height),color,thickness)
image = cv2.ellipse(image,(300,300),(100,50),0,0,180,155,5)

cv2.imshow("res",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
