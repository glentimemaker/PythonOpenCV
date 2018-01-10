import cv2
import numpy as np

img = cv2.imread('a.png', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 15) # color is BGR
cv2.rectangle(img, (50, 25), (200, 150), (255, 0, 255), 5)
cv2.circle(img, (100, 63), 55, (0,0,215), -1)

# Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# np.arrange(a,b,c) a is min, b is max, c is step
pts = pts.reshape((-1,1,2))
# reshape(-1, 2) does not know the row number.
cv2.polylines(img,[pts], True, (0,134,254), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'OpenCV Test!', (2,60), font, 10, (4,53,2))


cv2.imshow('image', img)
cv2.waitKey(0) # wait for any key to happen
cv2.destroyAllWindows()
