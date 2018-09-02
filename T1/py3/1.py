import numpy as np
import cv2 as cv
# Load an color image in grayscale
img = cv.imread("../img/lena.jpg", cv.IMREAD_UNCHANGED)

# cv.imread pode ser cv.IMREAD_COLOR, cv.IMREAD_GRAYSCALE, cv.IMREAD_UNCHANGED

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()