import numpy as np      

# Método de Runge-Kutta de terceira ordem
def runge_kutta(tempo, v0, y0, k, m, g, delta):
    S0 = np.array([v0, y0])
    i = 1
    alturaMaxima = y0
    tempoMaximo = tempo
    vF = 0
    #Roda enquanto não atingir o mar
    while (S0[1] >= 0):
        #Si + 1/2
        vIntermed = v0 + (delta/2) * (-g - (k/m * v0))
        yIntermed = y0 + (delta/2) * v0

        v1 = v0 + delta * (-g - (k/m * v0))
        y1 = y0 + delta * v0
        #Equações diferenciais
        F1 = (np.array([-g-(k/m * v0), v0]))
        F2 = (np.array([-g-(k/m * vIntermed), vIntermed]))
        F3 = (np.array([-g-(k/m * v1), v1]))
        #Si + 1
        S1 = S0 + delta *((1/6)*F1 + (4/6)*F2 + (1/6)*F3)

        tempo = tempo + delta
        i += 1
        vF = v0
        v0 = S1[0]
        y0 = S1[1]
        S0 = S1
        if y0 > alturaMaxima:
            alturaMaxima = y0
            tempoMaximo = tempo
    
    print("--- Delta = %f" %delta + " ---")
    print(f"Altura máxima alcançada:             = {alturaMaxima}")
    print(f"Tempo decorrido até a altura máxima  = {tempoMaximo}")
    print(f"Tempo total até a queda no mar       = {tempo-delta}")
    print(f"Velocidade no momento do impacto com o mar  = {abs(vF)}\n\n")

tempo = 0
#Velocidade inicial
v0 = 5
#Altura inicial
y0 = 200
k = 0.25
m = 2 
g = 10
i = 1 
while i <= 4:
    #deltas 0.1, 0.01, 0.001 e 0.0001
    delta = 10**(-i)
    runge_kutta(tempo, v0, y0, k, m, g, delta)
    i+=1