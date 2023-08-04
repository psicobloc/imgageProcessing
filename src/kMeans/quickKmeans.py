import numpy as np 
import cv2 as cv


def initCentroids(img, k):
    print("Initializing centroids")
    centroids = []
    centroids = img[np.random.randint(img.shape[0], size=k), np.random.randint(img.shape[1], size=k)]
    # print('Initial random centroids:')
    # print(centroids)
    # print('first centroid:')
    # print(centroids[0])
    return centroids


def resizeImg(img, ratio):
    resized = img 
    original_width = np.shape(img)[1]
    original_height = np.shape(img)[0]
    new_width =  int(original_width * ratio / 100)
    new_height =  int(original_height * ratio / 100)
    print(f"Resizing image from [{original_width}:{original_height}] to {ratio}% it's size: [{new_width}:{new_height}]")
    new_dimentions = (new_width, new_height)
    resized = cv.resize(img, new_dimentions, interpolation = cv.INTER_AREA)
    
    # cv.imwrite('resized2.jpg', resized)
    return resized
    

# 1- initialize centroids
# 2- assign a centroid index to each pixel (not changing the pixel value)
#   *2.1 Measure diference of each pixel with every centorid
#   *2.2 Assign to the pixel the closest centroid
# 3- Compute the avergae value of all the pixels in each group
# 4- change the value of each centroid to the average on it's group
# repeat <max_iters> times from #2
# make a copy of the image and change each pixel value to the value of 
# the centroid with the corresponding centroid_index










def main ():
    original_img = cv.imread('../../resources/stencil/agaveAlto.jpg')
    k = 10 
    max_iters = 10 
    resized_image = resizeImg(original_img, 25)
    centroids = initCentroids(resized_image, k)


if __name__ == '__main__':
    main()