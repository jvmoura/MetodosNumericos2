import numpy as np
from potenciaInversa import potenciaInversa

def potenciaDeslocamento(matrix, vetor, erro, mi, grau):
  A = np.subtract(matrix, (mi * np.identity(grau)))
  lambdaN, autovetorN = potenciaInversa(A, vetor, erro)
  lambdaI = lambdaN + mi
  print("----Método da Potência Com Deslocamento-----")
  print("Autovalor: ")
  print(lambdaI)
  print("Autovetor: ")
  print(autovetorN)
  print("--------------------------------------------")