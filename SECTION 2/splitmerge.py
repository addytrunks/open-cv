import cv2 as cv

img = cv.imread('Resources\image2.jpg')
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# The third dimension represents no of color channels.
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge((b, g, r))
cv.imshow('Merged', merged)

cv.waitKey(0)
