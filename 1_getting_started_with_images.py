import cv2
#https://www.youtube.com/watch?v=TGQcDaZ56ao

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
print("""\
To actualy display an image, we need to use the imshow function
cv2.imshow('Title for the window', img)  # Shows the image
cv2.waitKey(10000) # Decides how long to show an image for 10000 = 10 seconds
# using .waitKey() without any value will keep the image open indefinitely
""")
cv2.imshow('Sample Image', img)
cv2.waitKey(1000)
print("cv2.destroyAllWindows()# This command must be used to close all windows. ")
print("Later on we will learn how to close specific imges, but for now, this will do")
cv2.destroyAllWindows()

print("""\
To save an image, use the imwrite() function, which requires 2 input variables:
* the name and path of where we want to store the new image
* the img variable we created
cv2.imwrite('./data2/lena_copy.png', img)
""")
cv2.imwrite('./data2/lena_copy.png', img)


print("#############################################33")
print("Now we are going to make the code a little bit more useful")
print("If we press the esc key, the baboon image will close without saving")
print("If we press the s key, the baboon image will be closed and saved in data2")
print("""
img2 = cv2.imread('./data1/baboon.jpg', -1) # read the baboon image
#imshow to show the image
cv2.imshow('The Baboo: Press "s" to save and exit, or "esc" to exit without saving', img2)
k = cv2.waitKey(0) & 0xFF #This will wait for input from the key board
# the 0 & FF is recommend for 64-bit machines according to the documentation, but it's not strictly 
# mandatory

# And now an if to decide what to do when the 's' or 'esc' key is pressed
if k == 27: # 27 =  the esc key
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('./data2/baboon-copy', img2)
    cv2.destroyAllWindows()
""")

img2 = cv2.imread('./data1/baboon.jpg', -1)
cv2.imshow('The Baboo: Press "s" to save and exit, or "esc" to exit without saving', img2)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('./data2/baboon-copy', img2)
    cv2.destroyAllWindows()
