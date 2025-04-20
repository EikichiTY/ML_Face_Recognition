import cv2
import numpy as np
import os
import face_recognition
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread


class FaceRecognizerApp:
    def __init__(self, root, encodings_dir='encodings', tolerance=0.4):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("800x600+500+100")
        self.root.resizable(False, False)

        self.encodings_dir = encodings_dir
        self.tolerance = tolerance
        self.known_encodings = []
        self.known_labels = []
        self.video = None
        self.running = False

        self.label_video = tk.Label(root)
        self.label_video.pack()

        self.quit_button = tk.Button(root, text="Exit", command=self.quit_app, font=("Arial", 14), bg="red", fg="white")
        self.quit_button.pack(pady=10)

        self.load_mean_encodings()
    
    def load_mean_encodings(self):
        print("Loading mean encodings from:", self.encodings_dir)
        for file in os.listdir(self.encodings_dir):
            if file.endswith('_mean.npy'):
                label = file.replace('_mean.npy', '')
                path = os.path.join(self.encodings_dir, file)
                encoding = np.load(path)

                self.known_encodings.append(encoding)
                self.known_labels.append(label)
        print("Loaded labels:", self.known_labels)

    def recognize_faces(self, frame):
        if not self.known_encodings:
            return frame

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1].copy()

        face_locations = face_recognition.face_locations(rgb_small_frame)
        if not face_locations or not isinstance(face_locations[0], tuple):
            return frame

        try:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        except TypeError:
            return frame

        if not face_encodings:
            return frame

        for face_encoding, face_location in zip(face_encodings, face_locations):
            distances = face_recognition.face_distance(self.known_encodings, face_encoding)
            best_match_index = np.argmin(distances)

            if distances[best_match_index] <= self.tolerance:
                name = self.known_labels[best_match_index]
            else:
                name = "Unknown person"

            top, right, bottom, left = face_location
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return frame

    def update_frame(self):
        if not self.running:
            return
        ret, frame = self.video.read()
        if ret:
            frame = self.recognize_faces(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label_video.imgtk = imgtk
            self.label_video.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def start_recognition(self):
        print("Starting webcam...")
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            print("Error: Webcam not accessible.")
            return
        self.running = True
        self.update_frame()

    def quit_app(self):
        self.running = False
        if self.video:
            self.video.release()
        self.root.destroy()
        from gui.MainMenuApp import MainMenuApp
        new_root = tk.Tk()
        MainMenuApp(new_root)
        new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognizerApp(root)
    Thread(target=app.start_recognition).start()
    root.mainloop()

