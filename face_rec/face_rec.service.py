from functions.camera import init_camera, list_available_cameras
from functions.face_analysis import init_face_analysis, load_known_faces
from functions.face_recognition import recognition_worker
import queue
import threading
import time
import cv2

def run_face_recognition():
    # Initialize InsightFace
    app = init_face_analysis()

    # Load known faces
    image_directory = "saved_faces/"
    known_face_embeddings, known_face_ids = load_known_faces(image_directory, app)

    # List available cameras and allow user to choose one
    cameras = list_available_cameras()
    if not cameras:
        print("No cameras available!")
        exit(1)

    print("Available cameras:")
    for i, cam in enumerate(cameras):
        print(f"{i}: Camera {cam}")
    selected_index = int(input("Select the camera index: "))
    video_capture = init_camera(cameras[selected_index])

    # Prepare queues
    frame_queue = queue.Queue()
    request_queue = queue.Queue()

    # Start recognition worker thread
    recognition_thread = threading.Thread(target=recognition_worker, args=(frame_queue, request_queue, known_face_embeddings, known_face_ids), daemon=True)
    recognition_thread.start()

    frame_skip = 15
    frame_count = 0

    # Main loop
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to read frame. Exiting loop.")
            break

        resized_frame = cv2.resize(frame, (640, 640))  # Resize frame for InsightFace
        faces = app.get(resized_frame)

        face_locations = []
        embeddings = []

        for face in faces:
            bbox = face.bbox.astype(int)
            face_locations.append((bbox[1], bbox[2], bbox[3], bbox[0]))  # top, right, bottom, left
            embeddings.append(face.normed_embedding)

        # Skip frames for faster processing
        if frame_count % frame_skip == 0:
            frame_queue.put((frame, face_locations, embeddings))

        for face, (top, right, bottom, left) in zip(faces, face_locations):
            # Get the current width and height of the bounding box
            width = right - left
            height = bottom - top
            
            # Determine the size of the square based on the larger of the width or height
            square_size = max(width, height)

            # Calculate the center of the bounding box
            center_x = (left + right) // 2
            center_y = (top + bottom) // 2
            
            # Offset the square upwards by shifting the top a bit higher
            offset = square_size // 4  # This controls how much higher the square moves (adjust this value as needed)
            
            # Calculate the new coordinates for the square
            left = center_x - square_size // 2
            right = center_x + square_size // 2
            top = center_y - square_size // 2 - offset  # Move the square upwards
            bottom = top + square_size  # Adjust the bottom accordingly to keep the square size constant

            # Draw the square (with a yellow color and 1 pixel thickness)
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 225, 50), 1)  # Yellow square (BGR color)


        # Show video feed
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()
    frame_queue.put(None)
    recognition_thread.join()

if __name__ == "__main__":
    run_face_recognition()
