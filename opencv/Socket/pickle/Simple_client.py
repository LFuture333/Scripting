import cv2
import io
import socket
import struct
import time 
import pickle
import zlib
import numpy as np
import sys
from collections import namedtuple


cap = cv2.VideoCapture(0)




encoder_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]


#Declare the socket client parameters 
host = "192.168.0.16"
port = 100

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))
cam = cv2.VideoCapture(0)


img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    size = (640, 480)

    frame = cv2.resize(frame, size)

    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

cam.release()