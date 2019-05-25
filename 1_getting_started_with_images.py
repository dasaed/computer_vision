import cv2

print("Reading images using the OpenCV library")
print("cv2.imread('image', flag)")
print("""There are 3 types of flag values:
-1: Loads a color image
-2: Loas image in grayscale mode
-3: Loads image as such including alpha channel
example: """)
print("img = cv2.imread('data1/lena.jpg', 0)")
img = cv2.imread('data1/lena.jpg', 0)
print("""\
If you don't put the correct image, it will not generate any error. 
A good way to catch this error is to 'print the image'
print(img)
It will return 'None' if the image doesn't exist.
""")
print(img)

cv2.imshow('window', img)
