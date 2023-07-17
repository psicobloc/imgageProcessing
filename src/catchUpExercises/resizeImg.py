import cv2 as cv 


img1 = cv.imread('../../resources/stencil/agaveAlto.jpg')
scale_percent = 60 # percent of original image
width = int(img1.shape[1] * (scale_percent / 100))
height = int(img1.shape[0] * (scale_percent / 100))
dimTuple = (width, height)

# resize
imgResized = cv.resize(img1,dimTuple)

cv.imshow('resized img',imgResized)
cv.waitKey(5000)
cv.destroyAllWindows()
