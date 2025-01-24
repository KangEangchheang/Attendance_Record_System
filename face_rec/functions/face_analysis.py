import os
import cv2
from insightface.app import FaceAnalysis

# Initialize InsightFace
def init_face_analysis():
    app = FaceAnalysis(allowed_modules=["detection", "recognition"], verbose=False)
    app.prepare(ctx_id=0, det_size=(640, 640))  # Use CPU
    return app

# Function to load known face embeddings
def load_known_faces(image_dir, app):
    known_face_embeddings = []
    known_face_ids = []

    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            employee_id = os.path.splitext(filename)[0]
            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path)
            faces = app.get(image)
            if faces:
                known_face_embeddings.append(faces[0].normed_embedding)  # Use normalized embeddings
                known_face_ids.append(employee_id)
                print(f"Loaded face for {employee_id}")
            else:
                print(f"No face detected in {filename}. Skipping.")

    return known_face_embeddings, known_face_ids
