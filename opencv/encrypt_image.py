import cv2
import numpy as np
import sys


def xor_encrypt_decrypt(frame, key):
    frame_np = np.array(frame)

    key_np = np.array(key)

    key_np = np.resize(key_np, frame_np.shape)


    result = np.bitwise_xor(frame_np, key_np)

    return result


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



    encrypt_img = xor_encrypt_decrypt(frame=frame, key=key)

    jpg = cv2.imencode('.jpg', encrypt_img)

    print("Encrypt frame size: " + str(jpg))

    decrypted_image = xor_encrypt_decrypt(encrypt_img, key)


    combined_images = np.hstack((frame, encrypt_img, decrypted_image))


    cv2.imshow("Encrypt_img", combined_images)

    if (cv2.waitKey(1) == 27):
        break

cv2.destroyAllWindows()