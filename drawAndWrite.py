import cv2 as cv
import numpy as np

# img = cv.imread('Images/cat.jpg')
# cv.imshow('Cat', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# blank[:] = 0,255,0 # R G B
# cv.imshow('Green', blank)

cv.waitKey(0)

# 1. Paint the image a certain color

blank[200:300, 300:400] = 0,0,255 # R G B
# cv.imshow('Box', blank)

cv.waitKey(0)

# 2. Draw the rectangle

# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness = 2)
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness = -1)
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness = -1)
# cv.imshow('Rectangle', blank)

cv.waitKey(0)

#3. Draw a circle

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness = -1)
# cv.imshow('Circle', blank)

cv.waitKey(0)

#4. Draw a line

cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness = 3)
# cv.imshow('Line', blank)

cv.waitKey(0)

#5. Write text on image

cv.putText(blank, 'Hello', (blank.shape[1]//2,blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness = 2)
cv.imshow('Text', blank)
cv.waitKey(0)