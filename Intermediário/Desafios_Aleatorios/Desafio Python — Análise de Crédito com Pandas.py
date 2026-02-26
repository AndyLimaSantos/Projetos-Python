'''
Inicialmente temos que ter em mente oque cada parte do problema pede e oque podemos fazer para resolver ele
1- Analisando os banco de dados temos um dataframe, como são 3 data frames diferentes o caminho mais seguro
é para cada exigencia do problema criar um data frame que resolve esse nosso problema, outra forma é limpar
as planilhas que possuem mais informações que aquelas que desejamos, pode ser uma escolha. No entanto, por 
questão de segurança não irei mexer diretamente com as planilhas originais, um motivo é que caso precisemos 
de um backup podemos voltar a elas.

Logo a primeira coisa a se fazer é utilizar o pandas e criar um data frame de cada uma das panilhas. 

2- Total emprestado por cidade 
Para solucionar esse problema precisamos utilizar as duas primeiras planilhas, como o probema não exige que
tenhamos o valor pago, precisamos apenas associar os valores de if do cliente com o id de emprestimo e arma-
zenar aqueles que tem a mesma cidade.

3- Taxa de Inadimplência por faixa etária
Vamos precisar cacular a idade de cada cliente, e a partir disso gerar grupos de intervalos de idade, criar 
um data frame com a idade de cada um e se ele é inadimplente é uma boa, utilizaremos as duas primeiras tabe-
las. 

4- Criar um data frame de cada empréstimo com o valor inicial e o valor já quitado e depois o percentual 
utilizaremos a primeira e a terceira tabela.

'''
#___________________________________Importação das bibliotecas_________________________________________________
import pandas as pd #importamos a principal biblioteca que utilizaremos
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta

#____________________________________Criação das funções que nos auxiliam no projeto___________________________
def cria_taxa_inadimplencia(data,faixa_etaria):
    n_elementos_totais = int(data.shape[0])
    elementos_presentes = data["status"].value_counts()
    n_inadimplentes = int(elementos_presentes["inadimplente"])
    return {"Faixa_etaria":faixa_etaria, "Total_clientes":n_elementos_totais, "Inadimplentes":n_inadimplentes, "Taxa de Inadimplência":(n_inadimplentes/n_elementos_totais)}

def informacao_emprestimo(data,cliente):
    separa_per_emprestimo = {separa_per_emprestimo: grupo for separa_per_emprestimo, grupo in data.groupby('id_emprestimo')}
    lista_emprestimos = list(separa_per_emprestimo.keys())
    informacao_cliente = {"id_cliente":cliente,"Valor total pego":0,"Valor total pago":0,"Valor restante":0,"Percentual Quitado":0}
    for i in range(len(lista_emprestimos)):
        valor = separa_per_emprestimo[lista_emprestimos[i]]["valor"].unique()
        valor_pego = int(valor[0])
        informacao_cliente["Valor total pego"] += valor_pego
        valor_pago = int(separa_per_emprestimo[lista_emprestimos[i]]["valor_pago"].sum())
        informacao_cliente["Valor total pago"] += valor_pago
        valor_restante = valor_pego - valor_pago
        informacao_cliente["Valor restante"] += valor_restante
    informacao_cliente["Percentual Quitado"] += informacao_cliente["Valor total pago"]/informacao_cliente["Valor total pego"]
    return informacao_cliente

#______________________________Primeira parte se trata da leitura do banco de dados____________________________
clientes = pd.read_csv("Clientes.csv")  # importação do banco de clientes
emprestimos = pd.read_csv("Emprestimos.csv") # importação do banco de emprestimos
pagamentos = pd.read_csv("Pagamentos.csv") # importação do banco de pagamentos

#______________________________Formação do Banco de dados que usaremos no projeto______________________________
#criamos um dataframe com a data de hoje
date_atual = pd.DataFrame(data = {"id_cliente":np.arange(0,5000),"data_atual": ["2026-02-26"]*5000})
date_atual["data_atual"] = pd.to_datetime(date_atual["data_atual"])
#criamos um data com as idades
anos = (((date_atual["data_atual"]-pd.to_datetime(clientes["data_nascimento"]))/pd.Timedelta(days=1)).astype(int))//365
#Vamos criar dataframes com as informações importantes de cada um dos dataframes
data0 = pd.DataFrame(data = {"id_cliente":clientes["id_cliente"], "Idade":anos, "cidade":clientes["cidade"]})
data1 = pd.DataFrame(data = {"id_emprestimo":emprestimos["id_emprestimo"],"id_cliente":emprestimos["id_cliente"],"valor":emprestimos["valor"].astype(int), "status":emprestimos["status"]})
data2 = pd.DataFrame(data = {"id_emprestimo":pagamentos["id_emprestimo"], "valor_pago":pagamentos["valor_pago"]})
#vamos dar um merge para juntar as colunas que são interessantes de ter
data3 = pd.merge(data0,data1, how = "inner", on = "id_cliente")
data4 = pd.merge(data3,data2, how = "inner", on = "id_emprestimo")
#Banco de dados que iremos utilizar para resolver os problemas
data_opera = data4

#______________________________________Calculo do Valor emprestado por cidade____________________________________
cidades = {cidades: grupo for cidades, grupo in data_opera.groupby('cidade')}
chaves = list(cidades.keys())
total_emprestado = []
for i in range(len(chaves)):
    valor = int(cidades[chaves[i]]['valor'].sum())
    linha = {"cidade":chaves[i], "total_emprestado":valor}
    total_emprestado.append(linha)
valor_emprestado = pd.DataFrame(data=total_emprestado)

#________________________________taxa de inadimplencia por faixa etaria__________________________________________
#18-25
dado_intervalo1 = data_opera[(data_opera["Idade"]<25) & (data_opera["Idade"]>=18)]
resultado1 = cria_taxa_inadimplencia(dado_intervalo1,"18-25")
#25-40
dado_intervalo2 = data_opera[(data_opera["Idade"]<=40) & (data_opera["Idade"]>=25)]
resultado2 = cria_taxa_inadimplencia(dado_intervalo2,"25-40")
#41-60
dado_intervalo3 = data_opera[(data_opera["Idade"]<60) & (data_opera["Idade"]>=41)]
resultado3 = cria_taxa_inadimplencia(dado_intervalo3,"41-60")
#60+
dado_intervalo4 = data_opera[data_opera["Idade"]>=60]
resultado4 = cria_taxa_inadimplencia(dado_intervalo4,"60+")
#Criação do Dataframe.
inadimplecia_taxa = pd.DataFrame(data = [resultado1, resultado2, resultado3, resultado4])
#_________________________________Para os emprestimos ativos______________________________________________________
separa_per_status = {separa_per_status: grupo for separa_per_status, grupo in data_opera.groupby('status')}
dados_ativos = separa_per_status["ativo"]
#separando os clientes ativos.
separa_per_clientes = {separa_per_clientes: grupo for separa_per_clientes, grupo in dados_ativos.groupby('id_cliente')}
chaves = list(separa_per_clientes.keys())
#calculando a informação de cada cliente
data_emprestimo = []
for i in range(len(chaves)):
    dados_cliente_ativo = informacao_emprestimo(separa_per_clientes[chaves[i]],chaves[i])
    data_emprestimo.append(dados_cliente_ativo)
data_emprestimos_ativos = pd.DataFrame(data = data_emprestimo)