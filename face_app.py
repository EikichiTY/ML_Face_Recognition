import cv2 
import face_recognition
import numpy as np 


cam = cv2.VideoCapture(0)
cv2.namedWindow("Face Recognition App")

img_counter = 0


while True: 
    ret,frame =  cam.read()     
    if not ret: 
        print("fail to grab frame")
        break

    cv2.imshow("test",frame)

    #HOTKEYS 
    k = cv2.waitKey(1) 
    #escape key
    if k%256 == 27:                     
        print("Escape hit, closing the app")
        break
    #space key
    elif k%256 ==32: 
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("Screenshot taken")
        img_counter+=1 


cam.release()
cv2.destroyAllWindows()

