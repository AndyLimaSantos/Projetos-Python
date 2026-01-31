import pandas as pd
import numpy as np

arr2 = np.arange(100).reshape((10,10))
'''
Para criação de DataFrames, podemos utilizar o método .DataFRame(data = , index = , columns = )
'''

data1 = pd.DataFrame(arr2) #Cria um Data frame com os valores inseridos, ele gera as colunas e os indices sozinho, pois vc não passou isso.
#print(data1)
'''
Vamos criar duas listas para os indices e para as colunas
'''
colunas = "Brasil Argentina Russia USA China Bolivia Venezuela Franca Japao Coreia_do_Sul".split() #cria uma lista a partir dos espaços da string passada
linhas = "Fome Desemprego Moradia Habitacao Chuva Idosos Jovens Contribuentes Estudo PIB".split()

data2 = pd.DataFrame(data = arr2, index = linhas, columns= colunas) #Cria um novo data frame
print(data2)

'''
Podemos acessar pegar uma coluna e mortrar ela ou inserir ela em uma nova vaiavel.
'''

print(data2['Brasil']) #Retorna um dado do tipo Series com os valores presentes na coluna de nome indicado por voce
print(data2[['Brasil','Russia']]) #Retorna as colunas indexadas na lista informada.

'''
Podemos criar uma nova coluna
'''
data2["Australia"] = pd.Series(data = np.arange(10), index = linhas)
print(data2)

'''
Ou podemos somar duas colunas
'''
data2["Soma"] = data2['Brasil'] + data2['Australia']
print(data2)

'''
Podemos retirar colunas do DataFrame para isso utilizamso o .drop(nomeDaColuna, Axis = 1 ou 0, inplace = True)
Axis = 1 -> indica que vai retirar uma coluna
Axis = 0 -> Indica que será uma linha

O inplace serve para retirar a coluna dos dados reais, não apenas demonstrativo, se colocarmos False ele não retira dos dados..
'''
data2.drop("Soma", axis = 1, inplace=True)
print(data2)

'''
Podemos tirar as linhas, para isso fazemos com axis =0 e o nome será o nome da linha
'''

print(data2.drop("Chuva", axis=0, inplace=False))

'''
Podemos acessar as lihas utilizando os métodos .loc(nomeDaLinha) e .iloc('numero da linha')
vai devolver um dado do tipo Series também.
'''
print(data2)
print(data2.loc['Chuva'])
print(data2.iloc[4])