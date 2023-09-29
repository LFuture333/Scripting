import cv2
import numpy as np
import sys 
import base64

cap = cv2.VideoCapture(0)


size = (640, 480)

while True:

    ret, frame = cap.read()

    
    #Convert image to grey
    Gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Resizing the images 
    gray_rz = cv2.resize(Gray, size)
    color_rz = cv2.resize(frame, size)

    #Convert to base 64 format
    grey_txt = base64.b64decode(Gray)
    rzG_txt = base64.b64decode(gray_rz)

    color_txt = base64.b64decode(frame) 
    rzC_txt = base64.b64decode(color_rz)

    #get the size of variable 
    print("The size of original grey : ", sys.getsizeof(grey_txt) )
    print("The size of resize grey : ", sys.getsizeof(rzG_txt) )

    print("The size of original color: ", sys.getsizeof(color_txt))
    print("The size of resize color: ", sys.getsizeof(rzC_txt))
    