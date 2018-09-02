# Codigo exemplo do tutorial de opencv python do site oficial:
# https://docs.opencv.org/trunk/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print(str(width) + "x" + str(height))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
