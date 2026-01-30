'''

O objetivo agora é mostrar como acessar elementos internos a  um array de dimensão 1 e um array de dimensão 2
para que possamos fazer isso devomos entender como acessar os itens dentro de cada array

'''

import numpy as np

#criaremos um array de 5 itens e já modelaremos ele como uma matriz 5 x 5
arr = np.arange(25).reshape((5,5))
# para acessar os seus elementos devemos utilizar o método de incices
# podemos nesse caso usar dois blocos de conchetes ou utilizar apenas um bloco de conchete mas com virgula
elemento = arr[2][2]
elemento1 = arr[2,2] #esse método é mais usual, pois simplifica a escrita.

print(f"elemento = {elemento}")
print(f"elemento1 = {elemento1}")

'''
Algo não muito intuitivo é que quanto criamos uma array e queremos 
copia-los, o simbolo de receber "=" não cria a cópia que desejamos, 
ele apenas faz uma referência com outro nome a um mesmo espaço de 
memória. Para que possamos copiar o item devemos utilizar uma função 
nativa de copia do numpy, chamada .copy() 
'''

arr1 = np.arange(20).reshape(2,10)
arr2 = arr1[:5,:5] # não é uma cópia.

print(f"valor de arr1: \n{arr1}")
print(f"valor de arr2: \n{arr2}")

'''
Se modificarmos o arr2, modificaremos também o valor de arr1

'''
arr3 = np.arange(5)
arr4 = arr3.copy() #ou podemos fazer np.copy(arr3)

print(f"valor de arr3: {arr3}")
print(f"valor de arr4: {arr4}")