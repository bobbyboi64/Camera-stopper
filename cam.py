import cv2
import pyvirtualcam
import numpy as np
import keyboard

def toggle_toggle():
    global toggle
    toggle = not toggle

toggle = False
camera_list = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        camera_list.append(f"Camera {i}: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        cap.release()

print("Available cameras:")
for camera in camera_list:
    print(camera)


keyboard.add_hotkey("v", toggle_toggle)

while True:
    camera_choice = input("Choose a camera (0-9): ")
    if camera_choice.isdigit() and int(camera_choice) < len(camera_list):
        camera_choice = int(camera_choice)
        break
    else:
        print("Invalid camera choice.")

cap = cv2.VideoCapture(camera_choice)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

with pyvirtualcam.Camera(width=width, height=height, fps=30) as cam:
    print(f'Virtual camera created: {cam.device}')

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        key = cv2.waitKey(1)
        if toggle:

            cam.send(framenew)
        else:

            cam.send(frame_rgb)
            framenew = frame_rgb


        cam.sleep_until_next_frame()


cap.release()
