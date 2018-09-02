# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output_2.avi',fourcc, 20.0, (1280,720))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()