import cv2
import numpy as np
import sys
from collections import namedtuple


Image = namedtuple('Image', ['frame', 'key'])



cap = cv2.VideoCapture(0)
while True:

    #Capture fram from web
    ret,  frame = cap.read()


    #Frame resizing option
    size = (640, 480)

    #resize the frame to declare size
    frame = cv2.resize(frame, size)


 #encryption key
    key = np.random.randint(0,256, size=frame.shape, dtype=np.uint8)

    structure = Image(frame=frame, key=key)


    
    cv2.imshow("Encrypt_img", structure.frame)

    if (cv2.waitKey(1) == 27):
        break

cv2.destroyAllWindows()