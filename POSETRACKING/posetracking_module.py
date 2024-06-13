import cv2
import mediapipe as mp


class PoseTracking:
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        # To draw the hand landmarks (index,middle,thumb ...) and connect them.
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose

        # Parameters for the mediapipe pose module
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.pose = self.mpPose.Pose(static_image_mode=self.mode, min_detection_confidence=detectionCon,
                                     min_tracking_confidence=trackCon)

        self.results = None
        self.lmList = []

    # Returns the image with landmarks connected
    def findPose(self, image, draw=True):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(image, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return image

    # Returns a list with coordinates of each landmark
    def findPosition(self, image, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList
