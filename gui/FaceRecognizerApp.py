import os
import numpy as np
import face_recognition
import cv2
import tkinter as tk
from PIL import Image, ImageTk


class FaceRecognizerApp:
    def __init__(self, encoding_dir="encodings"):
        self.encoding_dir = encoding_dir
        self.known_encodings = {}
        self.load_encodings()

        self.window = tk.Tk()
        self.window.title("Live Face Recognition")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        self.video_label = tk.Label(self.window)
        self.video_label.pack()

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

    def load_encodings(self):
        for filename in os.listdir(self.encoding_dir):
            if filename.endswith("_mean.npy"):
                label = filename.replace("_mean.npy", "")
                path = os.path.join(self.encoding_dir, filename)
                self.known_encodings[label] = np.load(path)
        print(f"Loaded encodings for: {list(self.known_encodings.keys())}")

    def recognize_faces(self, frame):
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            label = "Unknown"
            color = (0, 0, 255)
            for name, known_encoding in self.known_encodings.items():
                match = face_recognition.compare_faces([known_encoding], encoding)[0]
                distance = face_recognition.face_distance([known_encoding], encoding)[0]
                if match:
                    label = f"{name} ({distance:.2f})"
                    color = (0, 255, 0)
                    break

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, label, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        return frame

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = self.recognize_faces(frame)
            frame = cv2.resize(frame, (800, 600))
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        self.window.after(10, self.update_frame)

    def on_close(self):
        self.cap.release()
        self.window.destroy()