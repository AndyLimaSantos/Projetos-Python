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
#______________________________________________________________________________________________________________
#Primeira parte se trata da leitura do banco de dados
clientes = pd.read_csv("Clientes.csv")  # importação do banco de clientes
emprestimos = pd.read_csv("Emprestimos.csv") # importação do banco de emprestimos
pagamentos = pd.read_csv("Pagamentos.csv") # importação do banco de pagamentos 

#______________________________________________________________________________________________________________
#vamos pegar o total emprestado por cidade.
#Para isso utilizaremos o merge, função do pandas para mesclas os valores, a partir de uma coluna especifica
#mesclaremos as duas tabelas de clientes e emprestimos a partir do id_cliente
dado_cidades = pd.merge(emprestimos,clientes, how = "inner", on = "id_cliente")

#______________________________________________________________________________________________________________
#Utilizaremso o groupby para criar um dict com os data frames de cada cidade, e usaremos esses datas frames para calcular 
#o valor final a partir de um novo dataframe.
cidades = {cidades: grupo for cidades, grupo in dado_cidades.groupby('cidade')}
chaves = list(cidades.keys())
total_emprestado = []
for i in range(len(chaves)):
    valor = int(cidades[chaves[i]]['valor'].sum())
    linha = {"cidade":chaves[i], "total_emprestado":valor}
    total_emprestado.append(linha)
valor_emprestado = pd.DataFrame(data=total_emprestado) 

#______________________________________________________________________________________________________________
'''
usamos essa linha para verificar se esta correto o valor total dos emprestimos
int(emprestimos['valor'].sum()) == int(valor_emprestado["total_emprestado"].sum())
'''

