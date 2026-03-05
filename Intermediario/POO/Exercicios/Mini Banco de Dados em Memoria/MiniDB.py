"""
O banco de dados vai ser um dicionario que contenha varias chaves com todos os nomes
de banco de dados presentes
banco de dados  = {"banco 1" = [], "banco 2" = [], ..., "banco n" = []}
Nas listas o indice 0 é o que contem o nome das colunas de cada banco d dados
"""



class miniDB:
    def __init__(self):
        #criar um banco de dados
        self.bancoDedados = {}
        self.colunas_dados = {}
        pass
    def create_table(self,nome_tabela, nome_colunas):
        #criar uma tabela interna ao banco de dados
        self.colunas_dados[nome_tabela] = nome_colunas
        self.bancoDedados[nome_tabela] = []
        pass
    def insert(self, nome, dados):
        self.bancoDedados[nome].append(dados)
        pass

    #O desafio é o select
    def select(self, nome_tabela, columns = None):
        if columns == None:
            pass
        pass
