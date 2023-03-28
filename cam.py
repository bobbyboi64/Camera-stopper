import cv2
import pyvirtualcam
import numpy as np
import keyboard

def toggle_toggle():
    global toggle
    toggle = not toggle

toggle = False
# Get the list of available cameras
camera_list = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        camera_list.append(f"Camera {i}: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        cap.release()

# Print the available cameras
print("Available cameras:")
for camera in camera_list:
    print(camera)


keyboard.add_hotkey("v", toggle_toggle)
# Ask the user to choose a camera
while True:
    camera_choice = input("Choose a camera (0-9): ")
    if camera_choice.isdigit() and int(camera_choice) < len(camera_list):
        camera_choice = int(camera_choice)
        break
    else:
        print("Invalid camera choice.")

# Initialize the chosen camera
cap = cv2.VideoCapture(camera_choice)

# Get the camera's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create the virtual camera
with pyvirtualcam.Camera(width=width, height=height, fps=30) as cam:
    print(f'Virtual camera created: {cam.device}')

    while True:
        # Read a frame from the existing camera
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Check if the 'q' key is pressed
        key = cv2.waitKey(1)
        if toggle:
            # If 'a' is pressed, freeze the camera by sending the last frame to the virtual camera
            cam.send(framenew)
        else:
            # If 'a' is not pressed, send the current frame to the virtual camera
            cam.send(frame_rgb)
            framenew = frame_rgb

        # Wait for the specified frame duration
        cam.sleep_until_next_frame()

# Release the camera
cap.release()
