import cv2 as cv

capture = cv.VideoCapture('Resouces/kitten.mp4')

# Scaling is done to make the image smaller or larger,so that the image can fit the screen and also can be processed faster
def rescaleFame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions  = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# This loop will keep running until the user presses the 'd' key
# The loop will keep reading the video frame by frame and displaying it
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()