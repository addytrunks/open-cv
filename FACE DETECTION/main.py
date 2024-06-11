import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cTime = 0
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:

    success, image = cap.read()

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            ih, iw, ic = image.shape
            # mpDraw.draw_detection(image,detection)
            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(image, bbox, (255, 0, 255), 2)
            cv2.putText(image, '{}%'.format(int(detection.score[0]*100)), (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(image, 'FPS:{}'.format(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.imshow('Video', image)
    cv2.waitKey(1)
