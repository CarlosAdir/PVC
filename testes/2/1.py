import numpy as np
import cv2 as cv

img = cv.imread('../img/messi.jpg')

px = img[100,100]
print( px )
# accessing only blue pixel
blue = img[100,100,0]
print( blue )

img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print( img.shape )
print( img.size )
print( img.dtype )

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow('imagem',img)
cv.waitKey(0)
cv.destroyAllWindows()