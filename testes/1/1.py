# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dc/d2e/tutorial_py_image_display.html


import numpy as np
import cv2 as cv
# Load an color image in grayscale
img = cv.imread("../img/lena.jpg", cv.IMREAD_GRAYSCALE)
# cv.imread pode ser cv.IMREAD_COLOR, cv.IMREAD_GRAYSCALE, cv.IMREAD_UNCHANGED

#cv.namedWindow('lena', cv.WINDOW_NORMAL) # Isso permite redimensionar a janela
cv.imshow('lena',img)
cv.waitKey(0)
cv.destroyAllWindows()


cv.imwrite('1/lena_gray.png',img)