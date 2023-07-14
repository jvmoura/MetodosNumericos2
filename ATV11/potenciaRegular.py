import numpy as np
from normalizar import normalizar

def potenciaRegular(matrix, vetor, erro):
  #Algoritmo
  lambda1_velho = 0
  lambda1_novo = 100
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
    vetorK_novo = np.matmul(matrix, autoVetor_velho)
    lambda1_novo = np.matmul(np.transpose(autoVetor_velho), vetorK_novo)
  print("---------Método da Potencia Regular---------")
  print("Autovalor dominante: ")
  print(lambda1_novo)
  print("Autovetor: ")
  print(autoVetor_velho)
  ##print("--------------------------------------------")