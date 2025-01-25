import cv2
import numpy as np
from .backend_request import send_recognition_request

import time

# Global dictionary to track recognized faces and the last time a request was sent
recognized_faces = {}
last_recognition_request_time = {}

# Function to process face recognition in the video stream
def recognition_worker(frame_queue, request_queue, known_face_embeddings, known_face_ids):
    while True:
        frame_data = frame_queue.get()
        if frame_data is None:
            break

        frame, face_locations, embeddings = frame_data
        try:
            current_time = time.time()  # Track time of recognition
            
            for face_embedding, (top, right, bottom, left) in zip(embeddings, face_locations):
                # Check if this face has already been recognized within the allowed timeout
                for recognized_id, (recognized_embedding, timestamp) in list(recognized_faces.items()):
                    similarity = np.dot(face_embedding, recognized_embedding)
                    
                    #the timout to get better performance 
                    if similarity > 0.6 and (current_time - timestamp < 5):  # Skip re-recognition for known faces within the timeout period
                        break
                else:
                    # Perform face recognition if not recognized already
                    distances = [np.dot(face_embedding, known_embedding) for known_embedding in known_face_embeddings]
                    max_similarity = max(distances)
                    if max_similarity > 0.4:  # Cosine similarity threshold
                        match_index = distances.index(max_similarity)
                        employee_id = known_face_ids[match_index]
                        print(f"Face recognized: {employee_id}")

                        # Store recognized face with its embedding and timestamp
                        recognized_faces[employee_id] = (face_embedding, current_time)

                        # Send HTTP request to backend
                        send_recognition_request(employee_id)

                        # Draw bounding box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

        except Exception as e:
            print(f"Error during face recognition: {e}")
