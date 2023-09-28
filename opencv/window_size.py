import cv2
import sys 
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    #Capture frame from web cam
    ret, frame = cap.read()

    #frame resizing option 
    size = (640, 480)

    #resize the frame to declare size
    resize = cv2.resize(frame, size)


#   Display the capture 
    cv2.imshow('Capture Resize', resize)

# if esc is press close the window
    if (cv2.waitKey(1) == 27):
        break
    cv2.destroyAllWindows()
