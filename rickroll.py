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

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Rick Ashley-Never Gonna Give You Up", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
oalQuit()

