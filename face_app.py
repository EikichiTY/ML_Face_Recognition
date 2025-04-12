import cv2 
import face_recognition
import numpy as np 
import os

label = input("Enter the label (ex: yacine): ")

# Create main path to save 
base_dir = "faces_dataset"
save_dir = os.path.join(base_dir, label)

# Create the folder if not existing
os.makedirs(save_dir, exist_ok=True)

cam = cv2.VideoCapture(0)
cv2.namedWindow("Face Recognition App")

img_counter = 0
while True: 
    ret,frame =  cam.read()     
    if not ret: 
        print("Failed to grab frame")
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
        img_name = f"{label}_{img_counter}.png"
        img_path = os.path.join(save_dir, img_name)
        cv2.imwrite(img_name,frame)
        print("Screenshot taken")
        img_counter+=1 

cam.release()
cv2.destroyAllWindows()

