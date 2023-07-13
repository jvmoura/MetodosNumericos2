import numpy as np
import scipy

def normalizar(vetorK_velho, vetorT):
  vetor = vetorK_velho/(scipy.linalg.sqrtm(np.matmul(vetorT, vetorK_velho), disp=True, blocksize=64))
  return vetor

def inserirDados(grau):
  i = 1
  j = 1
  matrix = []
  erro = 0
  vetor = []
  #Inserir dados da matriz
  v = 1
  #Inserir matriz
  while i <= grau:
    matrix_inter = []
    while j <= grau:
      print("Digite o %s" %(i) +"x"+"%s número: " % (j))
      num = float(input())
      matrix_inter.append(num)
      j+=1
    matrix.append(matrix_inter)
    i+=1
    j = 1
  #Vetor Arbitrario
  while v <= grau:
    vetor_inter = []
    print("Digite o %s digito do vetor arbitrario: " %(v))
    num = float(input())
    vetor_inter.append(num)
    vetor.append(vetor_inter)
    v+=1
  print("Digite o erro: ")
  erro = float(input())
  potenciaRegular(matrix, vetor, erro)

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
  print("Autovalor dominante: ")
  print(lambda1_novo)
  print("Autovetor: ")
  print(autoVetor_velho)

print("---------Método da Potência Regular---------")
print("1. Matrizes prontas")
print("2. Inserir matriz")
entrada = int(input())
if entrada == 1:
  matrix = [
        [5, 2, 1], 
        [2, 3, 1],
        [1, 1, 2]
    ]
  vetor = [
    [1],
    [1],
    [1]
  ]
  erro = 0.0001
  print("\nResultado da matriz 3x3: ")
  potenciaRegular(matrix, vetor, erro)
  matrix2 = [
        [40, 8, 4, 2, 1], 
        [8, 30, 12, 6, 2,],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5]
    ]
  vetor2 = [
    [1],
    [1],
    [1],
    [1],
    [1]
  ]
  print("\nResultado da matriz 5x5: ")
  potenciaRegular(matrix2, vetor2, erro)
if entrada == 2:
  print("Digite o grau da matriz:")
  grau = input()
  grau = int(grau)
  inserirDados(grau)