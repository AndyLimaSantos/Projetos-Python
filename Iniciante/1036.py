# Fórmula de Bhaskara
'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.
'''
def Delta(A,B,C):
    delta = B**2-4*A*C
    if delta < 0:
        return False
    return (delta)**(1/2)

def Raiz(delta, A, B):
    if delta != False:
        primeira_raiz = (delta - B)/(2*A)
        segunda_raiz = -(delta + B)/(2*A)
        return [primeira_raiz, segunda_raiz]
    else:
        return False

valores = input().split()  #leitura dos valores
A,B,C = float(valores[0]),float(valores[1]),float(valores[2]) #Separacao dos valores

if A == 0.0:
    print("Impossivel calcular")
else:
    valor = Raiz(Delta(A,B,C),A,B)
    if valor == False:
        print("Impossivel calcular")
    else:
        print(f'R1 = {valor[0]:.5f}\nR2 = {valor[1]:.5f}')