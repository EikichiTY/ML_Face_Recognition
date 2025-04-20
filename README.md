#  Facial Recognition App with CNN (Python)

## Description 

This project is a facial recognition application built in Python using a Convolutional Neural Network (CNN). It relies on the face_recognition library to detect and recognize faces in real time through a webcam.

Users can register themselves by taking photos directly from the interface. These images are saved in folders under the faces_dataset directory, with each folder representing a different person. During training, the app creates a 128-dimensional face encoding for each image and stores the results as .npy files. It also calculates the average encoding for each person.

When testing, the system activates the webcam and compares faces captured live to the saved encodings to recognize people in real time.

## Features 

- **Face Registration**  
  Users can take pictures of themselves directly through the interface. These images are saved in organized folders within the `faces_dataset` directory, each folder corresponding to a different identity.

- **Dataset Management**  
  Users can delete any dataset folder they created (except protected ones) via a dedicated GUI page.

- **Model Training & Testing**  
  When testing is triggered:
  - All stored face images are used to compute face encodings.
  - The average encoding per identity is saved as `.npy` files.
  - The webcam is then activated for **live testing**, comparing faces in real time with the known dataset.



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