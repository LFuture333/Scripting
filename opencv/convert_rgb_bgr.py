import cv2 
import numpy as np
import sys


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()



    #Resize the frame
    #frame resizing option 
    size = (640, 480)
    #resize the frame to declare size
    frame = cv2.resize(frame, size)

    #  Black & White
    Gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("b&w", Gray)
    cv2.imshow("RGB", frame)
    
    if (cv2.waitKey(1) == 27):
        break
cv2.destroyAllWindows()

