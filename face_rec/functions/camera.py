import cv2

# Function to list available cameras with error handling
def list_available_cameras(max_cameras=10):
    available_cameras = []
    
    for index in range(max_cameras):
        try:
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                available_cameras.append(index)
            cap.release()  # Always release the capture after checking
        except Exception as e:
            # Catch any exception and suppress the error message
            pass
    
    return available_cameras

# Function to initialize the camera
def init_camera(selected_index):
    cap = cv2.VideoCapture(selected_index, cv2.CAP_DSHOW)

    # Check if the camera opened successfully
    if not cap.isOpened():
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    return cap
