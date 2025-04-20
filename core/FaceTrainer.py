import os
import numpy as np
import face_recognition

class FaceTrainer:
    def __init__(self, dataset_dir="faces_dataset", save_dir="encodings"):
        self.dataset_dir = dataset_dir
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    def train_all(self):   #train all the database found in faces_dataset

        for file in os.listdir(self.save_dir):
            if file.endswith(".npy"):
                file_path = os.path.join(self.save_dir, file)
                os.remove(file_path)
                print(f"Deleted old encoding: {file}")

        labels = [d for d in os.listdir(self.dataset_dir)
                  if os.path.isdir(os.path.join(self.dataset_dir, d))]

        if not labels:
            print("No subfolders found in the dataset directory.")
            return

        for label in labels:
            print(f"\n=== Training for '{label}' ===")
            self.train(label)

    def train(self, label): #train model to recognize a label
        person_folder = os.path.join(self.dataset_dir, label)
        encodings = []

        for filename in os.listdir(person_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                path = os.path.join(person_folder, filename)
                print(f"Processing: {filename}")

                image = face_recognition.load_image_file(path)
                face_locations = face_recognition.face_locations(image)

                if not face_locations:
                    print(f"No face detected in {filename}")
                    continue

                encoding = face_recognition.face_encodings(image, face_locations)[0]
                encodings.append(encoding)

        if not encodings:
            print(f"No valid encodings found for '{label}'")
            return

        mean_encoding = np.mean(encodings, axis=0)
        self._save_encodings(label, encodings, mean_encoding)
        print(f"{len(encodings)} encodings saved for '{label}'.")

    def _save_encodings(self, label, encodings, mean_encoding):
        np.save(os.path.join(self.save_dir, f"{label}_encodings.npy"), encodings)
        np.save(os.path.join(self.save_dir, f"{label}_mean.npy"), mean_encoding)

    def load_mean_encoding(self, label):
        return np.load(os.path.join(self.save_dir, f"{label}_mean.npy"))

    def load_all_encodings(self, label):
        return np.load(os.path.join(self.save_dir, f"{label}_encodings.npy"), allow_pickle=True)

