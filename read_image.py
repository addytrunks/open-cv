import cv2 as cv

# Scaling is done to make the image smaller or larger,so that the image can fit the screen and can also  be processed faster
def rescaleFame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions  = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Takes in the path of the image and returns it in numerical format (matrix)
img = cv.imread('Resources/image.jpg')
resized_image = rescaleFame(img,0.25)

cv.imshow('Wallpaper',img)
cv.imshow('Wallpaper_resized',resized_image)

# Waits for a key to be pressed before closing the window
cv.waitKey(0)

