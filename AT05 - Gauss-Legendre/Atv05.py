import math
import numpy as np

def funcao(x):
    return np.cos(x)
    return y


tolerancia = 10**(-7)

def X_de_alfa(Xi, Xf, a):
        return (Xi+Xf)/2+((Xf-Xi)/2)*a

def definirQuantosPontos(a, b, pontos, N):
    if (pontos == 2):
        s = math.sqrt(1/3)
        raizesS = [s, -s]
        w = 1
        pesosW = [w, w]
        return Integracao(pesosW, raizesS, a, b, N)
    elif (pontos == 3):
        s = math.sqrt(3/5)
        raizesS = [s, 0, -s]
        w = 5/9
        w2 = 8/9
        pesosW = [w, w2, w]
        Integracao(pesosW, raizesS, a, b, N)
        return Integracao(pesosW, raizesS, a, b, N)
    elif (pontos==4):
         raizesS = [0.861136, -0.861136, 0.339981, -0.339981]
         w = 0.34785
         w3 = 0.65214
         pesosW = [w, w, w3, w3]
         Integracao(pesosW, raizesS, a, b, N)
         return Integracao(pesosW, raizesS, a, b, N)

def Integracao(pesosW, raizesS, xi, xf, N):
     resultado = 0
     resultadoSec = 0
     nDivisoes = 2**N
     #tamanho de cada subintervalo
     delta = (xf-xi)/nDivisoes

     for i in range(nDivisoes):
          xiAtual = xi + i*delta
          xfAtual = xiAtual + delta

          for alfaK, pesoK in zip(raizesS, pesosW):
               resultadoSec+=funcao(X_de_alfa(xiAtual,xfAtual,alfaK))*pesoK
     
     resultado = (xfAtual-xiAtual)/2 * resultadoSec

     return resultado


def main():
    print("Quadraturas de Gauss-Legendre")
    #xi = input("Digite o intervalo inicial: ")
    #xf = input("Digite o intervalo final: ")
    pontos = input("Digite a quantidade de pontos: ")
    pontos = int(pontos)
    xi = 0.0
    xf = 6.4*np.pi

    resultadoAnterior = definirQuantosPontos(xi, xf, pontos, 0)
    resultado = definirQuantosPontos(xi, xf, pontos, 1)
    i=1

    #Calcular erro para comparar com a tolerancia fornecida
    while(abs((resultado - resultadoAnterior)/resultado) > tolerancia):
         i+=1
         resultadoAnterior = resultado
         resultado = definirQuantosPontos(xi, xf, pontos, i)

    print("Gauss-Legendre com " + str(pontos) +  " pontos = " + str(resultado))
    print("Número de iterações = " + str(i))

main()