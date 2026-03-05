# Desafio — Monte um Mini Banco de Dados em Memória (Sem Pandas, Sem SQL)
## Objetivo
Implementar um mini sistema de banco de dados em memória, com:

    - Tabelas
    - Inserção de registros
    - Filtros
    - Seleção de coluna
    - JOIN simples
    - Agregaçãoiv
    - Tudo usando apenas:
    - listas
    - dicionários
    - classes
    - funções

## Requisitos

Implemente uma classe:

~~~python
class MiniDB:
    pass
~~~

Ela deve permitir:

    1. Criar tabela
    db.create_table("clientes", ["id", "nome", "idade"])

    2. Inserir registro
    db.insert("clientes", {"id": 1, "nome": "Ana", "idade": 25});

    3. Select simples
    db.select("clientes")

Retorna todos os registros.

    4. Select com filtro
    db.select("clientes", where=lambda row: row["idade"] > 18)

    5. Seleção de colunas
    db.select("clientes", columns=["nome"])
    6. JOIN simples (INNER JOIN)
    db.join(
        "clientes",
        "emprestimos",
        on=("id", "id_cliente")
    )

    7. Agregação

Implemente:

    db.aggregate(
        "emprestimos",
        group_by="id_cliente",
        operation="sum",
        column="valor"
    )

## Restrições

    Não usar pandas

    Não usar bibliotecas externas

    Não usar banco embutido

    Deve funcionar com milhares de registros

    Deve manter organização modular