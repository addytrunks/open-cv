import cv2
import numpy as np
from POSETRACKING import posetracking_module as ptm

cap = cv2.VideoCapture(0)
detector = ptm.PoseTracking()
count = 0
dir = 0

while True:
    succ, image = cap.read()
    if not succ:
        break
    image = detector.findPose(image, draw=False)
    lmList = detector.findPosition(image, draw=False)

    if len(lmList) != 0:
        # For left arm
        angle = detector.findAngle(image, 11, 13, 15)
        per = np.interp(angle, (200, 305), (0, 100))

        # check for the dumbbell curl
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 1
                dir = 0

    cv2.putText(image, f'REPS:{str(int(count))}', (30, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    cv2.imshow('Video', image)
    cv2.waitKey(10)
