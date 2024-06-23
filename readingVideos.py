import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4') ## 0 - webcam, 1- first cam connected, 2 - second cam connected

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()