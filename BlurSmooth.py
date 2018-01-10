import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    # Smooth
    kernel = np.ones((10,10), np.float32)/225
    smoothed = cv2.filter2D(frame, -1, kernel)

    # Gaussian Blur
    blur = cv2.GaussianBlur(frame, (151,151),0)

    # Median Blur
    median = cv2.medianBlur(frame, 15)

    # Bilateral Blur
    bilateral = cv2.bilateralFilter(frame, 15,75,75)

    cv2.imshow('smoothed', smoothed)
    cv2.imshow('frame', blur)
    cv2.imshow('median', median)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
