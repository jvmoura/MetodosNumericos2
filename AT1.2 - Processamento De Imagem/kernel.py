import numpy as np
import math
from matplotlib import pyplot as plt
from PIL import Image

def kernelGaussiano (kSize, sigma):
    kernel = np.zeros((kSize, kSize), np.float32)
    
    for i in range(kSize):
        for j in range(kSize):
            exp = (math.pow(1, 2) + math.pow(1, 2))/(2*math.pow(sigma, 2))
            kernel[i, j] = np.exp(-exp)/(2*np.pi*math.pow(sigma, 2))

    sum = np.sum(kernel)
    kernel = kernel/sum

    return kernel