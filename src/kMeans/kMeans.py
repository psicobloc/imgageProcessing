import sys 
import numpy as np 
import cv2 as cv

class k_means:
    def __init__(self, arg):
        self.k = int(arg[1])
        self.imgPath = arg[2] 
        self.max_iters = int(arg[3])
        # load image - 3D Array (r,g,b)
        # self.originalImg = 
        self.X = np.asarray(cv.imread(self.imgPath))
        # calculate centroids
        self.centroids = np.zeros((self.k, np.size(self.X, 1)))
        self.initCentroids()

    def initCentroids(self):
        self.idx = np.random.choice(self.X.shape[0], self.k, replace=False)
        self.centroids = self.X[self.idx]

    def findClosestCentroids(self):
        # index of the centroid assigned to example i
        self.idx = np.zeros((np.shape(self.X)[0], 1))
        # si tomamos la diferencia entre un ejemplo contra todas las clases
        # idx sera el indice del centroide con la menor diferencia
        # podeos vectorizar y sacar las k distancias de cada ejemplo al mismo tiempo
        # y luego tomamos solo la distancia menor, el indice de esa distancia menor esra idx
        for i in range(np.shape(self.X)[0]):
            self.idx[i] = np.argmin(np.sum(np.square(self.X[i,:] - self.centroids)))

    def computeCentroids(self):
        for iter in range(int(self.k)):
            indicesCentroide = (self.idx == iter).nonzero()
            print(indicesCentroide)
            sumaX = self.X[indicesCentroide,:].sum(axis=1)
            cuentaIndices = len(indicesCentroide[0])
            efe = (1/cuentaIndices)*sumaX
            ge = efe[0,:,:]
            print(iter)
            self.centroids[iter,:] = ge #(1/cuentaIndices)*sumaX #movemos el centroide al promedio

    def run(self):
        for i in range(self.max_iters):
            print(f"K-means iteration: {i} - max: {self.max_iters}")
            self.findClosestCentroids()
            self.computeCentroids()

def main (args):
    k_means_instance = k_means(args)
    k_means_instance.run()
    centroids = k_means_instance.centroids
    k_means_instance.findClosestCentroids()
    x_recovered = k_means_instance.centroids[k_means_instance.idx, :]
    cv.imwrite('recovered.jpg', x_recovered)
    
if __name__ == '__main__':
    args = sys.argv
    # k, img path, max_iters
    main(args)