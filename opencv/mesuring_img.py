#THIS code is not working for now 

#Note to self im working to encode the image stream for opencv handler

import cv2
import numpy as np
import sys
import base64

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

    retval, buffer = cv2.imencode('.jpg', Gray)

    jpg_as_text = base64.b64encode(buffer)

    text = np.char.encode(jpg_as_text, encoding=str, errors=None)

    print(jpg_as_text)

    print(len(jpg_as_text))
    break