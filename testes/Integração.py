
import matplotlib.pyplot as plt

#Vamos calcular a area sobre algum grafico.
def Base(a,b,N):
    delta_I = (b - a)/N
    return delta_I

def Integral_menor(a,b,N):
    area = 0
    base = Base(a,b,N)
    valor_base = a
    while valor_base < b:
        area += Funcao(valor_base)*base
        valor_base += base
    return area

def Integral_maior(a,b,N):
    area = 0
    base = Base(a,b,N)
    valor_inicial = a + base
    while valor_inicial <= b:
        area += Funcao(valor_inicial)*base
        valor_inicial += base
    return area

def Funcao(x):
    valor = x**2
    return valor



variacoes = input().split()
a,b,N = float(variacoes[0]),float(variacoes[1]),float(variacoes[2])

Area_maior = Integral_maior(a,b,N)
Area_menor = Integral_menor(a,b,N)
Valores_I_maior = []
Valores_I_menor = []
Diferenca = []
for i in range(10,10000):
    Area_maior = Integral_maior(a,b,i)
    Valores_I_maior.append(Area_maior)
    Area_menor = Integral_menor(a,b,i)
    Valores_I_menor.append(Area_menor)
    difere = Area_maior - Area_menor
    Diferenca.append(difere)



plt.plot(Valores_I_maior)
plt.plot(Valores_I_maior)
plt.plot(Diferenca)
plt.show()

