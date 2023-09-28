import cv2
import time


# Select the webcam 

cap = cv2.VideoCapture(0)


start_time = time.time()

#FPS update Time in seconds
display_time = 2
fc = 0
FPS = 0


while True:
    #Capture the web_cam stream
    ret, frame = cap.read()

    #Resize the frame
       #frame resizing option 
    size = (640, 480)

    #resize the frame to declare size
    frame = cv2.resize(frame, size)




    fc+=1
    TIME = time.time() - start_time


    if (TIME) >= display_time:
        FPS = fc / (TIME)
        fc = 0
        start_time = time.time()

    fps_disp = "FPS: " + str(FPS)[:5]


    # Add FPS count on frame
    image = cv2.putText(frame, fps_disp, (10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    

    #imshow converts bgr to rgb
    cv2.imshow("Video FPS", image)

    key = cv2.waitKey(1) & 0xFF


    if (key == ord("q")):
        break

cv2.destroyAllWindows()