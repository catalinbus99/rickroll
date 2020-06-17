#!/usr/bin/python

import cv2
import numpy as np
from openal import *

# open the video
cap = cv2.VideoCapture("rr.mp4")

if not cap.isOpened():
    print("Error: couldn't open file.")

# play the sound
source = oalOpen("rr.opus")
source.play()

window_name = "Rick Ashley-Never Gonna Give You Up"
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(window_name, 640, 360)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow(window_name, frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
oalQuit()

