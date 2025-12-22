import numpy as np
import cv2

image = np.zeros([512,512,3],np.uint8)*255

cv2.imshow("black image.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()