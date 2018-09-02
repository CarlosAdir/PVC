# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('../../input/video/hour.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
    	break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()