import numpy as np
# transfer function,vai fazer uma transferencia do valor do neuronio se ele foi
# ativado

def stepFunction(soma): # usado somente para problemas linearmente separadas 
    if(soma >= 1):
        return 1
    return 0

def sigmoidFunction(soma):#usada somente para problemas de classificaçao binarias
    return 1/(1 + np.exp(-soma))

def tahnFunction(soma):#usada somente para problemas de classificaçao
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def relu(soma):#usada para redes neurais para adicionar camadas
    if soma>=0:
        return soma
    return 0

def linear(soma):
    return soma

def softmax(x):#usada somente para problemas de classificaçao, quando voce tem mais de duas classes 
    ex = np.exp(x)
    return ex / ex.sum()

teste = stepFunction(5)
teste1 = sigmoidFunction(-5)
teste2 = tahnFunction(0.358)
teste3 = relu(-0.358)
teste4 = linear(0.358)

valores = [5.0,2.0,1.2]
print(softmax(valores))