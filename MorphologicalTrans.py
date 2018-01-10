import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([80, 20, 0])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Diffrent filter
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(res, kernel, iterations=1)
    dilation = cv2.dilate(res, kernel, iterations=1)

    # difference between input image and opening of the image TOPHAT
    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    # difference between the closing of the input image and input image BLACKHAT
    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('ero', opening)
    cv2.imshow('di', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()