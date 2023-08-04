import sys 
import numpy as np 
import cv2 as cv

class k_means:
    def __init__(self, arg):
        self.k = int(arg[1])
        self.imgPath = arg[2] 
        self.max_iters = int(arg[3])
        # load image - 3D Array (r,g,b)
        # self.original_img = 
        self.original_img = np.asarray(cv.imread(self.imgPath))
        ratio = 5 # to get the same image set 100; 
        new_width = int(np.shape(self.original_img)[1] * ratio / 100)
        new_height = int(np.shape(self.original_img)[0] * ratio / 100)
        self.new_dimentions = (new_width, new_height)
        #todo: make scaling optional with an arg
        scaled_img = cv.resize(self.original_img, self.new_dimentions, interpolation = cv.INTER_AREA)
        print("scaled img shape")
        print(np.shape(scaled_img))
        self.X = np.reshape(scaled_img, ((np.size(scaled_img,0)* np.size(scaled_img,1)),3))
        #self.X = self.X /255
        print("flattened img shape")
        print(np.shape(self.X))
        # a -3
        # calculate centroids
        self.centroids = np.zeros((self.k, np.size(self.X, 1)))
        self.initCentroids()

    def initCentroids(self):
        self.idx = np.random.choice(self.X.shape[0], self.k, replace=False)
        self.centroids = self.X[self.idx]
        print ('initCentroids - centroids')
        print(self.centroids)


    def findClosestCentroids(self):
        print('start - findClosestCentroids')
        # index of the centroid assigned to example i
        self.idx = np.zeros((np.shape(self.X)[0], 1))
        # si tomamos la diferencia entre un ejemplo contra todas las clases
        # idx sera el indice del centroide con la menor diferencia
        # podeos vectorizar y sacar las k distancias de cada ejemplo al mismo tiempo
        # y luego tomamos solo la distancia menor, el indice de esa distancia menor esra idx
        
        # print("shape:")
        # print(np.shape(self.X)[0])
        
        for i in range(np.shape(self.X)[0]):
            # print(f"iteration:{i}")
            squareDistance = np.square(self.X[i,:] - self.centroids)
            # print('square')
            # print(squareDistance)
            sum = squareDistance.sum(axis=1)
            # print('sum')
            # print(sum)
            argmin = np.argmin(sum)
            # print('argmin')
            # print(argmin)
            self.idx[i] = argmin
            #self.idx[i] = np.argmin(np.sum(np.square(self.X[i,:] - self.centroids)))
        print('end - findClosestCentroids - idx:')
        print(self.idx)

    def computeCentroids(self):
        print('start - computeCentroids')
        for iter in range(int(self.k)):
            indicesCentroide = (self.idx == iter).nonzero()[0]
            #print(indicesCentroide)
            sumaX = self.X[indicesCentroide,:].sum(axis=0)
            #print("sumaX:")
            #print(sumaX)
            cuentaIndices = len(indicesCentroide)
            efe = (1/cuentaIndices)*sumaX
            # ge = efe[0,:,:]
            # print(iter)
            self.centroids[iter,:] = efe #(1/cuentaIndices)*sumaX #movemos el centroide al promedio
        print('end - findClosestCentroids - centroids:')
        print(self.centroids)

    def run(self):
        for i in range(self.max_iters):
            #print(f"K-means iteration: {i} - max: {self.max_iters}")
            self.findClosestCentroids()
            self.computeCentroids()

def main (args):
    k_means_instance = k_means(args)
    k_means_instance.run()
    print('run finished')
    centroids = k_means_instance.centroids
    k_means_instance.findClosestCentroids()
    print('got closest centroids')
    print(k_means_instance.centroids)
    print('img')
    print(k_means_instance.X[0])
    newImage = repaintImg(k_means_instance.X, k_means_instance.idx, k_means_instance.centroids)
    #x_recovered = k_means_instance.centroids[k_means_instance.idx, :]
    # reshape image
    print('newImg[0]')
    print(newImage[0])
    print('new img shape 0')
    print(np.shape(newImage)[0])
    print('new img shape 1')
    print(np.shape(newImage)[1])
    finishedImg = np.reshape(newImage, (k_means_instance.new_dimentions[0], k_means_instance.new_dimentions[1], 3))
    print('finishedImg')
    print(finishedImg)
    print(finishedImg[0])
    cv.imwrite('recovered3.jpg', finishedImg)

def repaintImg(flatImg, idx, centroids):
    newImg = flatImg
    #newImg = [centroids[idx[np.where(flatImg == pixel)]] for pixel in flatImg] 
    # for indexCentroid, centroid in enumerate(centroids):
    #     newImg = [centroids[idx[flatImg.index(pixel)]] for pixel in flatImg]        
        
    #     # flatImg[indexCentroid] = centroid
    for i, centroidIdx in enumerate(idx):
        # print('centroidIdx')
        # print(centroidIdx)
        # print('i')
        # print(i)
        # print('centroidIdx[0]')
        # print(centroidIdx[0])
        # print('centroids[centroidIdx[0]]')
        # print(centroids[int(centroidIdx[0])])
        newImg[i] = centroids[int(centroidIdx[0])]

    
    return newImg

    


    
if __name__ == '__main__':
    args = sys.argv
    # k, img path, max_iters
    main(args)

    #///media/hugo/lentuchon/Documentos/openCV_codigos/imgProcForArt/imgageProcessing/src/kMeans/kMeans.py
    # python3 kMeans.py 7 ../../resources/stencil/agaveAlto.jpg 10
