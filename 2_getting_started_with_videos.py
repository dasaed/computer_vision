import cv2

print("Capturing video from your default camara")

print("""\
# Use the following command to capture an image from your default camara.
however, it will only capture a single image, so you need to create a while
loop to capture a video. The default camara is usually 0, or -1. If you have 
more camaras, you will want to try values greater thatn 1 (1,2,3,...,etc)

cap = cv2.VideoCapture(0) # Variable that stores the video

while(cap.isOpened()): #.isOpened() is a method that returns True or False, depending if the video source exists
    ret, frame = cap.read() # ret returns false if the camara doesn't work
                            # frame are the actual frames that you are capturing
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts video source into grayscale
    cv2.imshow('First Video', gray) # Displays the video in gray scale
    #cv2.imshow('First Video', frame) # Displays the video in normal mode
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit
        break

cap.release() # To release resources
cv2.destroyAllWindows() # closes all windows
""")

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*'XVID') #determines the codec for the video
out = cv2.VideoWriter('/tmp/sampleVideo1.avi', fourcc, 20.0, (640,480))
k = cv2.waitKey(0) & 0xFF

details = False
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        if details == False:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(cap.get(cv2.CAP_PROP_FPS))
            details = True
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('First Video', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
