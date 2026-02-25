'''
Vamos continuar ampliando nossos conhecimentos com o DataFrame, vamos analisar condicionais
'''
import numpy as np
import pandas as pd
#Vamso criar um array de 20 elementos novamente
Valores = np.linspace(0,10,20).reshape(2,10)
#Vamos criar uma lista novamente de 10 nomes
Alunos = "Maria Roberta Anais Luis Rodrigo Isabela Samanta Kleiton Brenda Thais".split()
#vamos criar um index novamente de 3 itens onde o terceiro é a soma dos outros dois
Index = "Nota_1 Nota_2".split()
#Cria o Banco de dados das notas
notasAlunos  = pd.DataFrame(data = Valores, index = Index , columns = Alunos)

'''
Vamos analisar agora os condicionais do data frame
'''
#Podemos retornar condicionais
#print(notasAlunos[notasAlunos > 2]) #Retorna um data frame comos NaN onde não satisfaz a condição
#Vamos inserir em  uma variavel

#Podemos fazer o mesmo só com a coluna
#print(notasAlunos["Anais"]>5) #Retorna uma Series com False e true

#Podemos resetar os index do dataframe tornando ele parte do banco de dados
print(notasAlunos.reset_index())
print(notasAlunos) #Ele não muda a planilha original a não ser que você peça
#Podemos inserir um novo index utilizando uma das colunas existentes o .set_index(nome da coluna)

'''
Lembrando que todas as alterações para serem gravadas devemos utilizar o inplace = True, 
isso muda o valor na memória não apenas no visual.
'''
#podemos utilizar funções de concatenação para juntar dataframes, com isso obtemos um data frame melhor
valor = np.zeros(10).reshape(1,10)
print(valor)
legenda = "media".split()
media = pd.DataFrame(data = valor, index = legenda, columns= Alunos)

'''
Podemos utilizar a função concatenar para obtermos um novo data frame
.concat([lista dos dataframes], axis = 0 ou 1)
se colocarmos axis = 1 ele concatena juntando na horizontal
se colocarmos axis = 0 ou não iserir o axis ele concatena na vertical
'''
Medias = pd.concat([notasAlunos, media]).copy() 
#Colocamos o copy() pois as funções do mandas só modificam a visualização
#não criam modificações na memória a não ser que você peça
'''
Agora podemos mudar o valor da media, mas para isso lembre que 
para trabaljhar com linhas utilizamos o Loc
'''
Medias.loc["media"] = (Medias.loc["Nota_1"] + Medias.loc["Nota_2"])/2
print(Medias)

'''
Caso usemos o concat com axis = 1 temos 
'''
Medias2 = pd.concat([notasAlunos, media], axis =1).copy()
print(Medias2)

'''
Existem outros operados como o Merge e o join, mas ficaremos apenas com o concat
.merge(left, right, how = "inner" , on = por qual coluna ele vai unificar )

dataframe1.join(dataframe2)
o join usa o primeiro dataframe como base e elimina mo segundo o que não temos no primeiro
'''

#Existe operações que você pode fazer com as colunas utilizando os métodos nativos também.