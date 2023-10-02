import numpy 
import cv2
import sys
import pickle



cap = cv2.VideoCapture(0)



encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cap.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size =  len(data)

    print(data)

    print('\n')
    
    print(size)
    sys.exit()