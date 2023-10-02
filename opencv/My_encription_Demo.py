import cv2
import  numpy as np
import sys
import base64

cap = cv2.VideoCapture(0)


size = (640, 480)

while True:
    ret, frame = cap.read()

    # Convert to grey 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Resize the images
    frame= cv2.resize(frame, size)

    #Converting image to binary buffer
