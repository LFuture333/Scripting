import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    #frame resizing option 
    size= (640, 480)


    #resize the frame
    resize = cv2.resize(frame, size)

    is_success, im_buf_arr = cv2.imencode('.jpg', resize)

    byte_im = im_buf_arr.tobytes()

    print(byte_im)
    break