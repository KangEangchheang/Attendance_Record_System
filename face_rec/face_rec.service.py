import cv2
import face_recognition
import requests
import os
import time

def list_available_cameras(max_cameras=10):
    available_cameras = []
    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()
    return available_cameras

# Load known faces and their IDs
def load_known_faces(image_dir):
    known_face_encodings = []
    known_face_ids = []

    for filename in os.listdir(image_dir): #employee images name should be ID+name
        if filename.endswith(".jpg") or filename.endswith(".png"):
            employee_id = os.path.splitext(filename)[0]  # Extract ID
            image_path = os.path.join(image_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]

            known_face_encodings.append(encoding)
            known_face_ids.append(employee_id)

    return known_face_encodings, known_face_ids

# Initialize known faces =========================================================================
image_directory = "saved_faces/"  # Directory containing employee images
known_face_encodings, known_face_ids = load_known_faces(image_directory)



# Initialize camera =========================================================================
cameras = list_available_cameras()
print("Available cameras:")
for i, cam in enumerate(cameras):
    print(f"{i}: Camera {cam}")
# Let the user choose a camera
selected_index = int(input("Select the camera index: "))
video_capture = cv2.VideoCapture(cameras[selected_index])


# when video capture is live
while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture video frame")
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect and encode faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            match_index = matches.index(True)
            employee_id = known_face_ids[match_index]

            # Send recognized employee ID to Nuxt server
            payload = {"employee_id": employee_id}
            try:
                response = requests.post("http://localhost:3000/api/mark-attendance", json=payload)
                print(f"Attendance marked for {employee_id}: {response.json()}")
            except requests.RequestException as e:
                print(f"Error sending data to Nuxt server: {e}")

    # Show video feed
    cv2.imshow("Video", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Cleanup
video_capture.release()
cv2.destroyAllWindows()
