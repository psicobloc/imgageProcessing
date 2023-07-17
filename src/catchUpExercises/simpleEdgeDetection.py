import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt

# read and show an image 

img1 = cv.imread('../../resources/stencil/agaveAlto.jpg', cv.IMREAD_GRAYSCALE)
#cv.imshow('agavote',img1)

# first we blur the image with a gaussian filter
# because Canny is susceptible to noise

scale_percent = 60 # percent of original image
width = int(img1.shape[1] * (scale_percent / 100))
height = int(img1.shape[0] * (scale_percent / 100))
dimTuple = (width, height)

# resize
imgResized = cv.resize(img1,dimTuple)

edges = cv.Canny(imgResized,100,200)
edges_inv = cv.bitwise_not(edges)
cv.imshow('edges del agavote', edges_inv)

# plt.subplot(121)
# plt.imshow(img1)
# plt.title('Original Image')
# plt.xticks([]) 
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(edges)
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# esto esta mal 
# fig, axs = plt.subplots(2)
# axs[0].imshow('original', imgResized)
# axs[1].imshow('original', edges)



fig, axs = plt.subplots(2)
axs[0].imshow(imgResized, cmap="gray")
axs[1].imshow(edges, cmap="gray")

# I can remove all the white and do a png,
# and then merge it with the original wiht some transparency
# so see what the edges look like on top of that img



#plt.show()




# Hysteresis Thresholding: I can experiment with random 
# max and min values for edge intensity, 
# and I could have the strongest edges be black, and softer edges
# be dark green? or light green? or smth... 







cv.waitKey(15000)
cv.destroyAllWindows()