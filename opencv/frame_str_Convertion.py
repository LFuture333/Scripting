import cv2
import numpy as np
import sys 


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    