import cv2
import numpy as np

img = cv2.imread("Amazon logo.jpg")
cv2.imshow("lion==",img)


# access a pixel value by its row and column co-ordinates.
px = img[233,150]  # store cordinate in variable.
print("the pixel of that co-ordinates",px)



# now try to find selected channel value from cordinate.
# we know we have three chanel - 0,1,2
# accessing onlt blue pixel.
blue = img[320,110,0]
print("The pixel having blue color==",blue)

grn = img[320,110,1]
print("the pixel having grn color==",grn)

red = img[320,110,2]
print("The pixel having red color==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()