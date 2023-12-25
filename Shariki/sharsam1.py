import cv2
import numpy as np
import random

cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cam = cv2.VideoCapture(0)

colors = {
    "yellow": ((28, 150, 238), (98, 227, 237)),
    "green": ((67, 121, 228), (144, 227, 120)),
    "blue": ((99, 226, 183), (182, 134, 20)),
    "orange": ((11, 161, 255), (94, 152, 255)),
}

color_sequence = random.sample(list(colors.keys()), 4)
print(f"Color sequence: {color_sequence}")

def display_result(frame, text):
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow("Result", frame)
    cv2.waitKey(0)  
    cv2.destroyWindow("Result")  

detected_colors = []

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_positions = []

    for color_name, (hsv_color, bgr_color) in colors.items():
        lower = (int(hsv_color[0] * 0.8), 50, 50)
        upper = (int(hsv_color[0] * 1.2), 255, 255)
        mask = cv2.inRange(hsvframe, lower, upper)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        if cnts:
            c = max(cnts, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(c)
            if radius > 30:  
                cv2.circle(frame, (int(x), int(y)), int(radius), bgr_color, 3)
                color_positions.append((int(y), color_name)) 
    cv2.imshow("Camera", frame)

    color_positions.sort(key=lambda c: c[0]) 

   
    midline = frame.shape[0] // 2
    top_half = [color_name for pos, color_name in color_positions if pos < midline]
    bottom_half = [color_name for pos, color_name in color_positions if pos >= midline]

    
    if len(top_half) == 2 and len(bottom_half) == 2:
        
        if sorted(top_half) == sorted(color_sequence[:2]) and sorted(bottom_half) == sorted(color_sequence[2:]):
            print("Отгадал!")
            display_result(frame, "Correct Sequence!")

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()