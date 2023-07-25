import sys 
import numpy as np 
import cv2 as cv




class k_means:
    def __init__(self, k: int, path: str, max_iters = 14):
        self.k = k
        self.imgPath = path 
        # load image - 3D Array (r,g,b)
        self.originalImg = np.asarray(cv.imread(path))
        # calculate centroids
        self.centroids = self.initCentroids(self.k, self.originalImg)


    def initCentroids (k,  mat):
        centroids = np.zeros(k, np.size(mat, 1))
        centroidIndexes = np.random.choice(mat.shape[0], k, replace=False)
        centroids = mat[centroidIndexes]
        return centroids

    def findClosestCentroids(X, centroids, k):
        # index of the centroid assigned to example i
        idx = np.zeros(np.shape(X)[0], 1)
        # si tomamos la diferencia entre un ejemplo contra todas las clases
        # idx sera el indice del centroide con la menor diferencia
        # podeos vectorizar y sacar las k distancias de cada ejemplo al mismo tiempo
        # y luego tomamos solo la distancia menor, el indice de esa distancia menor esra idx
        for i in range(np.shape(X)[0]):
            idx[i] = np.argmin(np.sum(np.square(X[i,:] - centroids)))
        return idx




    def runKmeans(X, initial_centroids, max_iters):
        rows, columns = np.shape(X)
        previous_centroids = centroids = initial_centroids
        idx = np.zeros((rows, 1))
        for i in range(max_iters):
            print(f"K-means iteration: {i} - max: {max_iters}")
            idx = self.findClosestCentroids(X, centroids)

    











def main (k, path):
    k_means_instance = k_means(k, path)

    
if __name__ == '__main__':
    k = int(sys.argv[0]) # size of K
    img_path = sys.argv[1] # path to image




    main()