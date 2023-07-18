import numpy as np
import math
from matplotlib import pyplot as plt
from PIL import Image
from kernel import kernelGaussiano

#Filtro Gaussiano
def filtroConvulacao(image, kernel):
    imageShape = image.shape
    kernelShape = kernel.shape
    saida = np.zeros(imageShape)

    bordaI = int((kernelShape[0] - 1)/2)
    bordaJ = int((kernelShape[1] - 1)/2)

    bordaImagem = np.zeros( ((imageShape[0] + 2*bordaI), (imageShape[1] + 2*bordaJ)))

    bordaImagem[bordaI: bordaImagem.shape[0] - bordaI, bordaJ: bordaImagem.shape[1] - bordaJ] = image

    for i in range(imageShape[0]):
        for j in range(imageShape[1]):
            saida[i, j] = np.sum(kernel * bordaImagem[i: i + kernelShape[0], j:j + kernelShape[0]])/kernelShape[0]
    return saida

def convolucao(image, kernel):
    imageShape = image.shape
    kernelShape = kernel.shape
    saida = np.zeros(imageShape)

    bordaI = int((kernelShape[0] - 1)/2)
    bordaJ = int((kernelShape[1] - 1)/2)

    bordaImagem = np.zeros( ((imageShape[0] + 2*bordaI), (imageShape[1] + 2*bordaJ)))

    bordaImagem[bordaI: bordaImagem.shape[0] - bordaI, bordaJ: bordaImagem.shape[1] - bordaJ] = image

    for i in range(imageShape[0]):
        for j in range(imageShape[1]):
            saida[i, j] = np.sum(kernel * bordaImagem[i: i + kernelShape[0], j:j + kernelShape[1]])
    return saida

image = Image.open('tuxedocat.png')
imageCinza = Image.open('tuxedocat.png').convert('L')
imageArray = np.asarray(image)
imageCinzaArray = np.asarray(imageCinza)

verm = imageArray[:, :, 0]; azul = imageArray[:, :, 1]; verde = imageArray[:, :, 2]
cinza = (0.3*verm + 0.3*verde+0.3*azul)/3

plt.imshow(cinza)
plt.show()
#Tamanho do Kernel
kernelSize = 9
kernel = kernelGaussiano(kernelSize, np.sqrt(kernelSize))

imageArray2 = filtroConvulacao(cinza, kernel)

plt.imshow(imageArray2)
plt.show()

sobelX = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])
sobelY = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

matrizA = convolucao(imageArray2, sobelX)
matrizB = convolucao(imageArray2, sobelY)

imageArray3 = np.sqrt(np.power(matrizA, 2) + np.power(matrizB, 2))

plt.imshow(imageArray3)
plt.show()

imageArray4 = np.zeros(imageArray3.shape)
#threshold
for i in range(imageArray3.shape[0]):
               for j in range(imageArray3.shape[1]):
                    if imageArray3[i, j] >= 0.5:
                         imageArray4[i, j] = 1.0
                    else:
                         imageArray4[i, j] = 0.0

imageFinal = np.zeros((imageArray4.shape[0], imageArray4.shape[1], 3))
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],0] = imageArray4
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],1] = imageArray4
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],2] = imageArray4

plt.imshow(imageFinal)
plt.show()

laplace1 = np.array([
     [0, -1, 0],
     [-1, 4, -1],
     [0, -1, 0]
])

laplace2 = np.array([
     [-1, -1, -1],
     [-1, 8, -1],
     [-1, -1, -1]
])

imageArray5 = convolucao(imageArray2, laplace1)
#threshold Laplace 2
imageArray6 = np.zeros(imageArray5.shape)
for i in range(imageArray5.shape[0]):
               for j in range(imageArray5.shape[1]):
                    if imageArray5[i, j] >= 0.4:
                         imageArray6[i, j] = 1.0
                    else:
                         imageArray6[i, j] = 0.0

imageFinal = np.zeros((imageArray6.shape[0], imageArray6.shape[1], 3))
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],0] = imageArray6
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],1] = imageArray6
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],2] = imageArray6

plt.imshow(imageFinal)
plt.show()
#threshold Laplace 2
imageArray7 = convolucao(imageArray2, laplace2)
imageArray8 = np.zeros(imageArray7.shape)
for i in range(imageArray7.shape[0]):
               for j in range(imageArray7.shape[1]):
                    if imageArray7[i, j] >= 0.4:
                         imageArray8[i, j] = 1.0
                    else:
                         imageArray8[i, j] = 0.0

imageFinal = np.zeros((imageArray8.shape[0], imageArray8.shape[1], 3))
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],0] = imageArray8
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],1] = imageArray8
imageFinal[0:imageFinal.shape[0], 0:imageFinal.shape[1],2] = imageArray8

plt.imshow(imageFinal)
plt.show()