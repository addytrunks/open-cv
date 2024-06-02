import cv2 as cv

img = cv.imread('Resources\image2.jpg')
cv.imshow('Cat',img)

# Averaging (finds the average of surrounding pixels)
average = cv.blur(img,(7,7))
cv.imshow('Average Blur',average)

# Gaussian blur
gaussian = cv.GaussianBlur(img,(5,5),0)
cv.imshow('Gaussian Blur',gaussian)

# Median (finds the median of surrounding pixels)
median = cv.medianBlur(img,5)
cv.imshow('Median Blur',gaussian)

cv.waitKey(0)