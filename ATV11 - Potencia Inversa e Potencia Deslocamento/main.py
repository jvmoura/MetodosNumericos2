from potenciaDeslocamento import potenciaDeslocamento
from potenciaInversa import potenciaInversa, printInversa
from potenciaRegular import potenciaRegular
  
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

print("\nResultados da matriz 1: ")
potenciaRegular(matrix, vetor, erro)
lambdaN, autovetorN = potenciaInversa(matrix, vetor, erro)
printInversa(lambdaN, autovetorN)
potenciaDeslocamento(matrix, vetor, erro, 3, 3)

matrix2 = [
      [-14, 1, -2], 
      [1, -1, 1],
      [-2, 1, -11],
  ]
vetor2 = [
  [1],
  [1],
  [1],
]
print("\nResultado da matriz 2: ")
potenciaRegular(matrix2, vetor2, erro)
lambdaN, autovetorN = potenciaInversa(matrix2, vetor2, erro)
printInversa(lambdaN, autovetorN)
potenciaDeslocamento(matrix2, vetor2, erro, 3, 3)
matrix3 = [
      [40, 8, 4, 2, 1], 
      [8, 30, 12, 6, 2,],
      [4, 12, 20, 1, 2],
      [2, 6, 1, 25, 4],
      [1, 2, 2, 4, 5]
  ]
vetor3 = [
  [1],
  [1],
  [1],
  [1],
  [1]
]
print("\nResultado da matriz 3: ")
potenciaRegular(matrix3, vetor3, erro)
lambdaN, autovetorN = potenciaInversa(matrix3, vetor3, erro)
printInversa(lambdaN, autovetorN)
potenciaDeslocamento(matrix3, vetor3, erro, 3, 5)
