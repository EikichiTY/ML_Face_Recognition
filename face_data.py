import face_recognition
import os

def load_known_faces(directory="."):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_face_encodings.append(encodings[0])
                name = os.path.splitext(filename)[0]  # use filename as name
                known_face_names.append(name)

    return known_face_encodings, known_face_names