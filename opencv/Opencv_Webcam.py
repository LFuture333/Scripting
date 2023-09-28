import cv2 as cv 
import sys
import cv2 as cv


def main():

    #Open Orbbec depth sensor 
    cap = cv.VideoCapture(0)

    while True:

        ret, img =  cap.read()
        cv.imshow('capture', img)

        if (cv.waitKey(1) == 27):
            break
    cv.destroyAllWindows()




main()