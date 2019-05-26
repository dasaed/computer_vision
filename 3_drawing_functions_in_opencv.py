import numpy as np
import cv2

img = cv2.imread('./data1/lena.jpg', 1)

print("img = cv2.line(image, tuple begining coordinates, tuple ending coordinate, color in inverse RGB (B, G, R), thickness)")
print("img = cv2.line(img, (0,0), (255,255), (0,0,255), 4)")
img = cv2.line(img, (0,0), (255,255), (0,0,255), 4)

print("no we are going to draw an arrow line")
img = cv2.arrowedLine(img, (255,255), (255,0), (0,255,0), 4)

print("Now we are going to draw a rectangle line")
print("img = cv2.rectangle(img, top_left_vertex(255,255), bottom_right_vertex(255,0), (255,0,0), 4)")
img = cv2.rectangle(img, (384,10), (500,128), (255,0,0), 6)
img = cv2.rectangle(img, (400,400), (500,450), (128,128,128),-1) # -1 means fill

print("Now we are going to draw a circle")
print("img = cv2.circle(img, center coordinates, radius, color, thicknes)")
img = cv2.circle(img, (100,400), 25, (0,255,255), 8)

font = cv2.FONT_HERSHEY_SIMPLEX
print("img = cv2.putText(img, 'text', starting coordinages, font face, font size, color, thickness, line type )")
img = cv2.putText(img, 'OpenCV', (200,300), font, 1, (255,255,255), 3, cv2.LINE_AA )



cv2.imshow('Sample image 1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("Now we are going to create an image from 0")
print("img2 = np.zeroes([height,width,3],np.uint8) # this method gives you a black image of 512x512 ")
img2 = np.zeros([512,512,3],np.uint8)
img2 = cv2.putText(img2, 'OpenCV', (256,256), font, 1, (255,255,255), 3, cv2.LINE_8)
cv2.imshow("second example", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

