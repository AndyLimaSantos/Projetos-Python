import numpy as np #Importamos a biblioteca Numpy para nosso sistema.

'''
Vamos trabalhar agora com a criação de arrays, 
os arrays são apenas objetos que possuem uma 
estrutur melhor para trabalharmos matemáticamente.
'''
lista = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(lista) #o método exige que seja uma lista como argumento.

'''
Temos maneiras melhores de fazer matrizes maiores
sem inserir ou escrever as linstas nós mesmos.
'''

#utilizando o método .arange() -> recebe tanto um valor númérico como varios parâmetros de start, stop, step.

arr1 = np.arange(10)  # >>> [0,1,2,3,4,5,6,7,8,9]
print(arr1)
arr2 = np.arange(0,10)  # >>> [0,1,2,3,4,5,6,7,8,9]
print(arr2)

'''
Uma escolha muitas vezes é criarmos uma matriz preenchida com 1's
e 0's e modificar os elementos dessa matriz após termos ela criada já
existe algumas maneiras de fazer isso. Utilizando dois métodos o zeros
e o ones.

.zeros()
.ones()

ambos recebem um elemento númérico ou uma tupla.
'''

arr3 = np.zeros(5) #criar um array linha de 5 elementos com valor 0 em cada elemento
print(arr3)
arr4 = np.zeros((5,5)) #cria uma matriz array com 25 elementos de valor 0 distribuidos em 5 linhas e 5 colunas
print(arr4)
arr5 = np.ones(5)  #criar um array linha de 5 elementos com valor 1 em cada elemento
print(arr5)
arr6 = np.ones((5,5))  #cria uma matriz array com 25 elementos de valor 1 distribuidos em 5 linhas e 5 colunas
print(arr6)

'''
Podemos criar arrays com valores dentro de um determinado intervalo
definido por start, stop, e o ultimo parametros sendo o número de elementos.
'''

arr7 = np.linspace(0,1,10)
print(arr7)
arr8 = np.linspace(0,2,50)
print(arr8)

'''
Podemos agora fazer o seguinte, trabalhar com matrizes onde os valores da diagonal,
são modificados

.eye(linha, coluna)
recebe uma tupla com o número de linhas e colunas que a matriz deve ter
e coloca o  valor 1 nos indices i=j

.diag(matriz ou array)
recebe uma matriz e substitui a diagonal com essa matriz

'''

arr9 = np.eye(5,5)
print(arr9)
arr10 = np.eye(4,9)
print(arr10)
arr11 = np.eye(5)
print(arr11)

matriz = np.arange(5)
arr12 = np.diag(matriz)
print(arr12)

arr13 = np.diag(arr12)  #nesse caso ele devolve a diagonal da matriz (l,c)
print(arr13)

'''
Podemos pegar o shape da matriz, ou seja, obter o numero de linhas e colunas utilizando o shape.
E podemos modemos modificar o shape da matriz utilizando o reshape.
'''
arr14 = np.arange(25)
print(arr14)
arr15 = arr14.reshape((5,5))
print(arr15)
print(arr14.shape, arr15.shape)

'''
Podemos também verificar algumas coisas, o valor maximo e o valor minimo de cada array, assim como identificar a localização desses valores.
Para isso utilizamos os métodos 
.max()
.min()
.armax()
.argmin()
'''
