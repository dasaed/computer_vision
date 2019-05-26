import cv2

print("Capturing video from your default camara")

cap = cv2.VideoCapture(0) # Variable that will capture the camara frames

#fourcc = determines the codec of the video, and there are 2 ways of using this:
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#out = cv2.VideoWriter('output file name', codec, fps, Tuple(width,height)) #This is how we save the video to a file
out = cv2.VideoWriter('./sampleVideo1.avi', fourcc, 20.0, (640,480))


details = False # I used this variable so that we are not posting the details at every frame
while(cap.isOpened()): # check if there is a video input. Returns false if the video input doesn't exist
    ret, frame = cap.read() # ret = False if there isn't a frame detected. frame = the actual frame we are seeing
    if ret == True: # if we do detect video input, show it and save it
        if details == False:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(cap.get(cv2.CAP_PROP_FPS))
            details = True
        out.write(frame) # writes the input video to file
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts the input video to gray scale
        cv2.imshow('First Video', gray) # shows the gray image. if we change gray to frame, it would
        # display the normal image
        #if cv2.waitKey(1) & 0xFF == 27: if we want to exit with the esc key
        if cv2.waitKey(1) & 0xFF == ord('q'): # exits with the 'q' key
            break
    else:
        break

# Now we need to release all the resources. Similar to how we should close a file after we are done working with it
cap.release()
out.release()
cv2.destroyAllWindows()
