    def recognize_faces(self, frame):
        if not self.known_encodings:
            print("No known encodings loaded.")
            return frame

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1].copy()  # <- COPY is IMPORTANT for face_recognition

        face_locations = face_recognition.face_locations(rgb_small_frame)

        # Prevent error when face_locations is empty or invalid
        if not face_locations or not isinstance(face_locations[0], tuple):
            return frame

        try:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        except TypeError as e:
            print("Encoding error:", e)
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