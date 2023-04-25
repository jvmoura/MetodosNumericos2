import math

def funcao(x):
    return math.pow(math.sin(2*x)+ 4*(x)**2 + 3*x, 2)

tolerancia = 10**(-6)

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

def Integracao(pesosW, raizesS, a, b, N):
     resultado = 0
     resultadoSec = 0
     nDivisoes = 2**N
     delta = (b-a)/nDivisoes

     for i in range(nDivisoes):
          xi = a + i*delta
          xf = xi + delta

          for alfaK, pesoK in zip(raizesS, pesosW):
               resultadoSec+=funcao(X_de_alfa(xi,xf,alfaK))*pesoK
     
     resultado = (xf-xi)/2 * resultadoSec

     return resultado


def main():
    print("Quadraturas de Gauss-Legendre")
    a = input("Digite o intervalo inicial: ")
    b = input("Digite o intervalo final: ")
    pontos = input("Digite a quantidade de pontos: ")
    pontos = int(pontos)
    a = int(a)
    b = int(b)

    resultadoAnterior = definirQuantosPontos(a, b, pontos, 0)
    resultado = definirQuantosPontos(a, b, pontos, 1)
    i=1

    #Calcular erro para comparar com a tolerancia fornecida
    while(abs(resultadoAnterior-resultado) > tolerancia):
         i+=1
         resultadoAnterior = resultado
         resultado = definirQuantosPontos(a, b, pontos, i)

    print("Gauss-Legendre com " + str(pontos) +  " pontos = " + str(resultado))
    print("Número de iterações = " + str(i))

main()
