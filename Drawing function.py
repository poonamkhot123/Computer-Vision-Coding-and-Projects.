# Drawing functions in openCV

import numpy as np
import cv2

image = cv2.imread("Amazon logo.jpg")
# image = cv2.resize(image,(600,700))

image = cv2.line(image,(0,0),(200,200),(154,92,424),8)

cv2.imshow("res",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
