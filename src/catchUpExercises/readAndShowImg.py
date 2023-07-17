import cv2 as cv  

# read and show an image 

img1 = cv.imread('../../resources/stencil/agaveAlto.jpg')
cv.imshow('agavote',img1)
cv.waitKey(5000)
cv.destroyAllWindows()