import numpy as np
import scipy

def normalizar(vetorK_velho, vetorT):
  vetor = vetorK_velho/(scipy.linalg.sqrtm(np.matmul(vetorT, vetorK_velho), disp=True, blocksize=64))
  return vetor  