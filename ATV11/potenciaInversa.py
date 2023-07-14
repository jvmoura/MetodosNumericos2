import numpy as np
import scipy
from normalizar import normalizar

def potenciaInversa(matrix, vetor, erro):
  #Algoritmo
  #Decomposição LU
  P, L, U = scipy.linalg.lu(matrix)
  lambda1_velho = 0
  lambda1_novo = 100
  lambdaN = 0
  autovetorN = 0
  vetorK_novo = vetor
  vetorK_velho = []
  autoVetor_velho = 0
  mt = []
  vetorK_velho = vetorK_novo
  mt = np.transpose(vetorK_velho)
  while abs((lambda1_novo-lambda1_velho)/lambda1_novo) > erro:
    lambda1_velho = lambda1_novo
    vetorK_velho = vetorK_novo
    mt = np.transpose(vetorK_velho)
    autoVetor_velho = normalizar(vetorK_velho, mt)
    #SolverLU
    vetorK_novo = np.matmul(np.linalg.inv(matrix), autoVetor_velho)
    lambda1_novo = np.matmul(np.transpose(autoVetor_velho), vetorK_novo)
  lambdaN = 1/lambda1_novo
  autovetorN = autoVetor_velho
  return lambdaN, autovetorN

def printInversa(lambdaN, autovetorN):
  print("---------Método da Potência Inverso---------")
  print("Autovalor: ")
  print(lambdaN)
  print("Autovetor: ")
  print(autovetorN)