# Desafio Python — Análise de Crédito com Pandas
## Contexto

Você trabalha em uma fintech e recebeu três bases de dados já carregadas como DataFrames.

📦 Dados de Entrada - Bancos de Dados

clientes

~~~python
clientes = [
    {"id_cliente": 1, "nome": "Ana", "data_nascimento": "1998-05-10", "cidade": "São Paulo", "data_cadastro": "2022-01-01"},
    {"id_cliente": 2, "nome": "Bruno", "data_nascimento": "1985-07-20", "cidade": "Rio de Janeiro", "data_cadastro": "2021-06-15"},
    {"id_cliente": 3, "nome": "Carla", "data_nascimento": "1970-02-11", "cidade": "São Paulo", "data_cadastro": "2020-09-10"},
]
~~~
emprestimos
~~~python
emprestimos = [
    {"id_emprestimo": 101, "id_cliente": 1, "valor": 5000, "taxa_juros": 0.02, "data_contratacao": "2023-01-10", "status": "ativo"},
    {"id_emprestimo": 102, "id_cliente": 2, "valor": 8000, "taxa_juros": 0.03, "data_contratacao": "2023-02-15", "status": "inadimplente"},
    {"id_emprestimo": 103, "id_cliente": 3, "valor": 12000, "taxa_juros": 0.015, "data_contratacao": "2023-03-01", "status": "quitado"},
]
~~~
pagamentos
~~~python
pagamentos = [
    {"id_pagamento": 1, "id_emprestimo": 101, "valor_pago": 1000, "data_pagamento": "2023-02-01"},
    {"id_pagamento": 2, "id_emprestimo": 101, "valor_pago": 1500, "data_pagamento": "2023-03-01"},
    {"id_pagamento": 3, "id_emprestimo": 103, "valor_pago": 12000, "data_pagamento": "2023-04-01"},
]
~~~
# Parte 1 — Transformação e Análise

Usando pandas, implemente:

## Total emprestado por cidade

Resultado esperado:
~~~python
cidade            total_emprestado
São Paulo         XXXX
Rio de Janeiro    XXXX
~~~
## Taxa de inadimplência por faixa etária

Faixas:
1. 18–25
2. 26–40
3. 41–60
4. 60+

Calcule:
~~~python
faixa_etaria    total_clientes    inadimplentes    taxa_inadimplencia
~~~

## Top 5 clientes por valor contratado

Ordene pelo valor total de empréstimos.

## Para cada empréstimo ativo, calcule:

    1. Valor total já pago
    2. Valor restante
    3. Percentual quitado

# Parte 2 — Engenharia de Dados

Implemente uma função:
~~~python
def gerar_score_risco(clientes_df, emprestimos_df):
    pass
~~~
Ela deve gerar um score simples, por exemplo:

    +2 pontos por empréstimo inadimplente
    +1 ponto por mais de 2 empréstimos ativos
    -1 ponto se todos os empréstimos estiverem quitados

Retorne um DataFrame final com:
~~~
id_cliente
nome
total_emprestimos
inadimplencias
score_risco
~~~

# Parte 3 — Nível Avançado

Sem usar merge diretamente:

Reimplemente pelo menos uma análise usando:

1. groupby
2. map
3. apply
4. ou dicionários intermediários


# O que esse desafio testa

1. Manipulação de DataFrame
2. JOIN (merge)
3. groupby
4. Agregações
5. Engenharia de features
6. Pensamento analítico
7. Organização de código
8. Clareza estrutural