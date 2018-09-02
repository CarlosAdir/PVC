# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dc/d2e/tutorial_py_image_display.html

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../img/lena.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()