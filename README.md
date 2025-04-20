#  Facial Recognition App with CNN (Python)

## Description 
The objective of this project is to develop a facial recognition model using neural networks (supervised learning) in Python. The model used is a Convolutional Neural Network (CNN). It used with a webcam implementation to identify whether image contains the face of a specific person. Real-time face detection and classification are performed using a webcam to showcase the model's ability to differentiate the target person from others. All known faces are stored in folders inside the faces_dataset folder. The name of the folder provides the label.

This project uses the face_recognition library to recognize faces in real time using a webcam. During training, face encodings (128-value vectors) are extracted from images in faces_dataset/ and saved as .npy files. These files store both individual encodings and their average (_mean.npy) for each person. Later, during testing, the system loads these .npy files to identify faces live from the webcam by comparing the live encoding to the saved ones.

## Features 

## Technologies Used 
- Python 3.x
- `face_recognition`
- `dlib`
- `opencv-python`
- `numpy`
- `Pillow`
- `Tkinter` (standard GUI library)

## How to run 
1. Install dependencies: 
   ```bash
   pip install -r requirements.txt

2. Launch the main interface: 
    ```bash
    python main.py 