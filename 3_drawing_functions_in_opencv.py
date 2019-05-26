import numpy as np
import cv2

img = cv2.imread('./data1/lena.jpg', 0)



cv2.imshow('Sample image 1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
