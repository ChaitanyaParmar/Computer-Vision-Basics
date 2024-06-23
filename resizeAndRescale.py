import cv2 as cv

def rescaleFrame(frame, scale = .75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4') ## 0 - webcam, 1- first cam connected, 2 - second cam connected

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

## Resizing image

# import cv2 as cv

# img = cv.imread('Images/cat.jpg')
# cv.imshow('Cat', img)

# def rescaleFrame(frame, scale = .75): ## this method works for images, videos. live video
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
    
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# while True:
#     cv.imshow('Image', resized_image)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# cv.destroyAllWindows()

## Another method

# import cv2 as cv

# def changeRes(width, height): ## works only for live video i.e webcam
#     capture.set(3, width)
#     capture.set(4,height)

# capture = cv.VideoCapture('Videos/dog.mp4')