import cv2 as cv
import numpy as np

img = cv.imread('Resources/image2.jpg')

# Translate: x = no of pixels to move in x direction, y = no of pixels to move in y direction
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
cv.imshow('Translated',translated)

# Rotate
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        # Rotate around the center
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,90)
cv.imshow('Rotated',rotated)

# Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flipping
# 0 -> Vertical Flip, 1 -> Horizontal Flip, -1 -> Both
flip = cv.flip(img,0)
cv.imshow('Flipped',flip)

cv.waitKey(0)