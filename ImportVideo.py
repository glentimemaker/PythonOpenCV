import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # number is the capture time
# if capture the existed video, parameter is the video name.
fourcc = cv2.cv.CV_FOURCC(*'XVID') #VideoWriter_fourcc(*'XVID') video code type
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()  # ret is true or false captured
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.waitKey() returns a 32 Bit integer value (might be dependent on the platform).
        # The key input is in ASCII which is an 8 Bit integer value.
        # So you only care about these 8 bits and want all other bits to be 0.
        break

cap.release()
out.release()
cv2.destroyAllWindows()
