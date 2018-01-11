import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create a BFMatcher object with distance measurement cv2.NORM_HAMMING (since we are using ORB)
# and crossCheck is switched on for better results.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Then we use Matcher.match() method to get the best matches in two images.
# We sort them in ascending order of their distances
# so that best matches (with low distance) come to front.
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# Then we draw only first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2,kp2, matches[:10], None, flags=2)

plt.imshow(img3)
plt.show()
