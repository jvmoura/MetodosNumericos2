import numpy as np      

# Método de Runge-Kutta de terceira ordem
def preditorCorretor(tempo, v0, y0, k, m, g, delta):
    vVelho = v0
    yVelho = y0

    S = np.array([vVelho, yVelho, 0, 0, 0, 0, 0, 0])
    for i in range(1, 4):
        S1 = np.array(((-g - (k/m)*vVelho), vVelho))
        v2 = vVelho + (delta/2) * S1[0]
        S2 = np.array(((-g - (k/m)*v2), v2))
        v3 = vVelho + (delta/2 * S2[0])
        S3 = np.array(((-g - (k/m)* v3), v3))
        v4 = vVelho + (delta * S3[0])
        S4 = np.array(((-g - (k/m)*v4), v4))

        S[i*2] = vVelho + (delta/6.0)*(S1[0] + 2*S2[0] + 2*S3[0] + S4[0])
        S[i*2 + 1] = yVelho + (delta/6.0)*(S1[1] + 2*S2[1] + 2*S3[1] + S4[1])

        vVelho = S[i*2]
        yVelho = S[i*2 + 1]

    t = 0.0
    vVelho = v0
    vNovo = yVelho
    yVelho = y0
    yNovo = yVelho
    while yNovo > 0:
        SN1 = np.array(((-g - (k/m) * S[0]), S[0]))
        SN2 = np.array(((-g - (k/m) * S[2]), S[2]))
        SN3 = np.array(((-g - (k/m) * S[4]), S[4]))
        SN4 = np.array(((-g - (k/m) * S[6]), S[6]))
        #Predição
        r = np.array([0, 0])
        r[0] = S[6] + (delta/24) * (-9 *SN1[0] + 33 * SN2[0] - 59 * SN3[0] + 55 * SN4[0])
        r[1] = S[7] + (delta/24) * (-9 *SN1[1] + 33 * SN2[1] - 59 * SN3[1] + 55 * SN4[1])

        f = np.array(((-g - (k/m) * r[0]), r[0]))
        #Correção
        vNovo = S[6] + (delta/24) * (SN2[0] - 5 * SN3[0] + 19 * SN4[0] + 9 * f[0])
        yNovo = S[7] + (delta/24) * (SN2[1] - 5 * SN3[1] + 19 * SN4[1] + 9 * f[1])
        t+=delta
        if vVelho * vNovo < 0:
            if yNovo < yVelho:
                alturaMax = yVelho
                tempoMax = t - delta
            else:
                alturaMax = yNovo
                tempoMax = t
            
        if yVelho*yNovo < 0:
            vF = vVelho
            tF = t - delta
        
        temp = S[2:]
        temp = np.append(temp, vNovo)
        temp = np.append(temp, yNovo)

        S = temp
        vVelho = vNovo
        yVelho = yNovo
    
    print("--- Delta = %f" %delta + " ---")
    print(f"Altura máxima alcançada:             = {alturaMax}")
    print(f"Tempo decorrido até a altura máxima  = {tempoMax}")
    print(f"Tempo total até a queda no mar       = {tF-delta}")
    print(f"Velocidade no momento do impacto com o mar  = {abs(vF)}\n\n")

tempo = 0
#Velocidade inicial
v0 = 5
#Altura inicial
y0 = 200.0
k = 0.25
m = 2.0
g = 10.0
i = 1 
while i <= 4:
    #deltas 0.1, 0.01, 0.001 e 0.0001
    delta = 10**(-i)
    preditorCorretor(tempo, v0, y0, k, m, g, delta)
    i+=1