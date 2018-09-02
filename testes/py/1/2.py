# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dc/d2e/tutorial_py_image_display.html

import numpy as np
import cv2 as cv
img = cv.imread('../../input/img/lena.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
	cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
	cv.imwrite('../../output/img/lena_gray.png',img)
	cv.destroyAllWindows()