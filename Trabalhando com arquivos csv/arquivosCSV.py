'''
Para trabalharmos com arquivos CSV precisamos inicialmente que o arquivo esteja inserido na mesma pasta que o programa. 
utilizaremos pandas pois nosso objetivo é trabalhar com as tabela sexternas.
'''
import pandas as pd

#vamos ler o arquivo csv com uso do método .read_csv(Nome do arquivo) que pode ser modificado para
#leitura de outros tipo de arquivo.

dados = pd.read_csv("Intentionalhomicides.csv")
print(dados.columns)