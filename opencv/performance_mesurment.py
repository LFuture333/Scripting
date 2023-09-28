import cv2
import time

cap = cv2.VideoCapture(0)


t_Start = time.time()
time1 = 0



while True:
    e1 = cv2.getTickCount()
    ret, frame = cap.read()

    #frame resizing option 
    #size = (640, 480)

    #resize the frame to declare size
    #frame = cv2.resize(frame, size)



    
    cv2.imshow("Cam", frame)
    e2 = cv2.getTickCount()
    time1 = (e2 - e1)/ cv2.getTickFrequency() + time1

    elapsedTime= time.time() - t_Start  # stop
    print(elapsedTime)

    #If user press "q" close program
    key = cv2.waitKey(1) & 0xFF
    if (key == ord("q")):
        break

cv2.destroyAllWindows()