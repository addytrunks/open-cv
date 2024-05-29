import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), np.uint8)

# 1.Paint the image a certain color (Square)
blank[200:300,300:400] = 0,0,255
cv.imshow('Blank', blank)

# 2. Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)

# fills the rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)

# dynamic rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)

cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text', blank)

cv.waitKey(0)