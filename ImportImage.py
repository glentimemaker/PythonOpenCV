import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('a.png', cv2.IMREAD_GRAYSCALE)
# read the image with alpha channel, or 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() # press any key the window will closed
# cv2.imwrite('a2.png', img)
# waitKey(0) will display the window infinitely until any keypress (it is suitable for image display)
# waitKey(25) will display a frame for 25 ms

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()




