'''
Precisamos primeiro chamar a funcao do Pandas
para fazermos  isso chamamos a biblioteca 

import pandas as pd
'''
import pandas as pd
import numpy as np

# Series, podem ser criadas com listas, dicionarios e ate mesmo arrays
arr = np.arange(5) # criar um array de 5 elementos
list = [i for i in range(5)] # cria uma lista de 5 elementos começando do 0
bib = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'} # cria uma biblioteca
# print(f"{arr}\n{list}\n{bib}")
'''
Vamos criar uma Series a partir desses 3's
'''
ser1 = pd.Series(arr)
ser2 = pd.Series(list)
ser3 = pd.Series(bib)
#print(f'{ser1}\n{ser2}\n{ser3}')

'''
Como não passamos o index, ele insere um index automatico,
logo ele substitui o index por uma númeração começando do 
0 até o ultimo numero do item passado.
'''

#Podemos passar o index, veja
lista = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

ser4 = pd.Series(data = arr , index = lista)
ser5 = pd.Series(data = list , index = lista)
ser6 = pd.Series(data = bib , index = lista) 

#print(f'{ser4}\n{ser5}\n{ser6}')
'''
No entanto perceba que quando inserimos i index
em uma bibioteca, ele retorna NaN, pois não existe
correspondencia na bibliotea com o indices passados.

Para podermos acessar os elementos na Series, devemos 
utilizar a mesma lógica de lista
'''
ser7 = pd.Series(np.arange(10))
print(ser7) 
print(ser7[0]) #Retorna o elemento na posição 0.
print(ser7[1:3]) #Retorna o elemento na posição 0 até o 3 sem incluir o elemento na posição 3.

'''
Podemos também mexer com as condicionais, como podemos ver aqui.
'''

print(ser7 > 2) #retorna uma Series de Booleanos com True e False que satisfazem a condição inserida.
'''
Podemos visualizar os valores, utilizando a condicional dentro do index.
'''
print(ser7[ser7>4]) #retorna uma Series apenas com os itens que satisfazem as condições.
