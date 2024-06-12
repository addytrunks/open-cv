import cv2
import time
from HANDTRACKING import handtracking_module as htm

# Set camera width and height
wCam, hCam = 640, 480

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Set width
cap.set(4, hCam)  # Set height

# Initialize hand detector
detector = htm.HandDetector(detectionCon=0.8)

# Landmark IDs for the tips of the thumb, index, middle, ring, and pinky fingers
tipIds = [4, 8, 12, 16, 20]

# Initialize previous and current time for FPS calculation
pTime = 0
cTime = 0

while True:
    # Read frame from webcam
    succ, img = cap.read()

    if not succ:
        break

    # Detect hands in the frame
    img = detector.findHands(img)
    # Get positions of hand landmarks
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        # Check if thumb is up
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Check if other fingers are up
        for id in range(1, len(tipIds)):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Display the number of fingers up
        if fingers.count(1) == 0:
            cv2.putText(img, f"Number:6", (20, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=4)
        else:
            cv2.putText(img, f"Number:{fingers.count(1)}", (20, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=4)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{str(int(fps))}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    # Show the image with detected hands and FPS
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
