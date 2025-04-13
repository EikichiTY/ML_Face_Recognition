import os
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import joblib

data = []
labels = []

base_path = "faces_dataset"
for label in os.listdir(base_path):
    folder = os.path.join(base_path, label)
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        data.append(img.flatten())
        labels.append(label)

X = np.array(data)
y = np.array(labels)

# Réduction de dimension
pca = PCA(n_components=100).fit(X)
X_pca = pca.transform(X)

# SVM
model = SVC(kernel='linear', probability=True)
model.fit(X_pca, y)

# Sauvegarde
joblib.dump((model, pca), "face_model.pkl")
print("Model trained and saved.")