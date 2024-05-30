# Contours are useful tools for shape analysis and object detection and recognition.

import cv2 as cv
import numpy as np

img = cv.imread('Resources/image2.jpg')
blank = np.zeros(img.shape, dtype='uint8')

grayScaled = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(grayScaled, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

# Finding contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# drawContours(image, contours, contour_index (-1 to include add contours), color, thickness)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)