# Switch between colour spaces
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("Resources/image2.jpg")

# Matplotlib reads image in RGB which is inverse of BGR format
# plt.imshow(img)
# plt.show()

# Conversions from BGR to other colour scales
# Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# Similarly conversions can be done the other way round

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR',hsv)

cv.waitKey(0)