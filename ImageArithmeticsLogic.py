import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
# img2 = cv2.imread('mainsvmimage.png')
img2 = cv2.imread('mainlogo.png')

# Threshold
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255,cv2.THRESH_BINARY_INV) # 220 is threshold
cv2.imshow('python', mask)
mask_invisible = cv2.bitwise_not(mask)
# Black out the area of logo in ROI. Otherwise the add operation is not working
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_invisible)
# Take only the area of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
# The number 13 is represented by 00001101. Likewise,
# 17 is represented by 00010001. The bit-wise AND of 13 and 17 is therefore 000000001, or 1

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('result', img1)


# Adding image together

# add = img1+img2
# add2 = cv2.add(img1,img2)

# weighted = cv2.addWeighted(img1,0.6, img2, 0.4, 0)
# cv2.imshow('weight', weighted)

#

cv2.waitKey(0)
cv2.destroyAllWindows()
