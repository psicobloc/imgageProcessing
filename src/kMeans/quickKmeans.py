import numpy as np 
import cv2 as cv


def initCentroids(img, k):
    centroids = []
    print (img[0][0])

def resizeImg(img, ratio):
    resized = img 
    original_width = np.shape(img)[1]
    original_height = np.shape(img)[0]
    new_width =  int(original_width * ratio / 100)
    new_height =  int(original_height * ratio / 100)
    print(f"Resizing image from{original_width}:{original_height} with ratio {ratio} to {new_width}:{new_height}")
    new_dimentions = (new_width, new_height)
    resized = cv.resize(img, new_dimentions, interpolation = cv.INTER_AREA)
    
    # cv.imwrite('resized2.jpg', resized)
    return resized
    











def main ():
    original_img = cv.imread('../../resources/stencil/agaveAlto.jpg')
    k = 10 
    max_iters = 10 
    resized_image = resizeImg(original_img, 25)
    centroids = initCentroids(resized_image, k)

if __name__ == '__main__':
    main()