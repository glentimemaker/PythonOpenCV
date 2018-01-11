import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
# These are arrays used by the algorithm internally. Just Do It
# Gaussian Mixture Model(GMM) is used to model the foreground and background
fgdModel = np.zeros((1,65), np.float64)

rect = (161, 79, 150, 150) # in this region

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0,1).astype('uint8')
#  all 0-pixels and 2-pixels are put to 0 (ie background)
# and all 1-pixels and 3-pixels are put to 1(ie foreground pixels).
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
