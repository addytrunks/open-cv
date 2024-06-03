import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# To draw the hand landmarks (index,middle,thumb ...) and connect them.
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, image = cap.read()

    # To laterally invert the image
    # image = cv2.flip(image, 1)

    # Convert the BGR to RGB because the mediapipe uses only RGB
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # To check whether a hand is detected in the image.
    if results.multi_hand_landmarks:
        # The loop is to draw the landmarks/points for 'n' hands.
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # id: gives us the landmark id (eg, 0: wrist,1 : thumb), lm : gives us the coordinates of each landmark
                # print(id, lm)
                h, w, c = image.shape
                # Converting the coordinates/landmarks to pixels by multiplying it with width and height, which we can use it to our benefit
                cx, cy = int(lm.x * w), int(lm.y * h)

                # To use the landmark
                # if id == 8:
                #     cv2.circle(image, (cx, cy), 10, (0, 0, 0), cv2.FILLED)
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    # Logic to calculate the FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Displaying FPS
    cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    cv2.imshow('Video', image)
    cv2.waitKey(1)