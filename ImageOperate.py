import cv2
import numpy as np

img = cv2.imread('a.png', cv2.IMREAD_COLOR)

px = img[55,55]

img[55,55] = [255,255,255]

img [100:150,22:144] = [255,255,255]
roi = img [100:150,22:144]
img [0:50, 0:122] = roi

cv2.imshow('imageChanged', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
