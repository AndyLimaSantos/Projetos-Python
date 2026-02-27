'''
Solução do Problema abaixo
'''
#___________________________________Importação das bibliotecas_________________________________________________
import pandas as pd #importamos a principal biblioteca que utilizaremos
import numpy as np
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

def gerar_score_risco(clientes, emprestimos):
    #correção dos dataframes que entram, filtragem apenas para as colunas que realmente nos interessam
    data_cliente = pd.DataFrame(data = {"id_cliente":clientes["id_cliente"],"Nome":clientes["nome"], "Idade":anos, "cidade":clientes["cidade"]})
    data_emprestimo = pd.DataFrame(data = {"id_emprestimo":emprestimos["id_emprestimo"],"id_cliente":emprestimos["id_cliente"],"valor":emprestimos["valor"].astype(int), "status":emprestimos["status"]})
    #mesclar as tabelas para uma única que será a tabela do score
    data_score = pd.merge(data_cliente, data_emprestimo, how = "inner", on = "id_cliente")
    #separa as tabela e insere em um dicionário, com as chaves sendo a id de cada cliente.
    separa_per_cliente= {separa_per_cliente: grupo for separa_per_cliente, grupo in data_score.groupby('id_cliente')}
    chaves_separa_per_cliente = list(separa_per_cliente.keys())     #guarda as chaves que servirão de acesso ao dict
    #primeiro laço que vai entrar em cada um dos clientes e analizar a sua situação
    gerar_score = []
    for i in range(len(chaves_separa_per_cliente)):
        analise_cliente = separa_per_cliente[chaves_separa_per_cliente[i]]
        nome = analise_cliente["Nome"].unique()[0]
        #separar agora os todos os emprestimos que tivemos e guardalos em um dict
        separa_per_emprestimos = {separa_per_emprestimos: grupo for separa_per_emprestimos, grupo in analise_cliente.groupby('id_emprestimo')}
        separa_per_emprestimo_key = list(separa_per_emprestimos.keys())
        #vamos criar os valores da linha de cada cliente
        total_emprestimos, score_risco, total_inadimplencias = len(separa_per_emprestimo_key), 0, 0
        #iniciamos um novo laço, com as informações que buscamos de cada cliente, de maneira a atualizar os dados dele para o ultimo dataframe.
        ativos, quitados = 0, 0
        for m in range(len(separa_per_emprestimo_key)):
            status = separa_per_emprestimos[separa_per_emprestimo_key[m]]['status'].unique()[0]
            if status == "inadimplente":
                score_risco += 2
                total_inadimplencias += 1
            if status == "ativo":
                ativos += 1
                if ativos > 2:
                    score_risco += 1
                    ativos = 0
            if status == "quitado":
                quitados += 1
                if quitados == total_emprestimos:
                    score_risco -= 1
        linha_cliente = {"id_cliente":chaves_separa_per_cliente[i], "Nome":nome,"total_emprestimos":total_emprestimos,"Quitados":quitados, "Inadimplencias":total_inadimplencias, "Score_risco":score_risco}
        gerar_score.append(linha_cliente)
    return pd.DataFrame(data = gerar_score)
#__________________________________Solução do Problema_________________________________________________________
def main():
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
    valor_emprestado = pd.DataFrame(data=total_emprestado) #----> Solução

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
    inadimplecia_taxa = pd.DataFrame(data = [resultado1, resultado2, resultado3, resultado4]) #----> Solução
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
    data_emprestimos_ativos = pd.DataFrame(data = data_emprestimo) #----> Solução
    #_____________________________________Engenharia de dados_________________________________________________________
    gerar_score_risco(clientes, emprestimos) #----> Solução

if __name__ == "__main__":
    main()
