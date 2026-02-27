# Desafio Python — Motor de Avaliação de Regras (Mini Rule Engine)
## Objetivo

Implemente um sistema capaz de:
- Receber um conjunto de dados (ex: registros de usuários).
- Receber uma lista de regras lógicas configuráveis.
- Avaliar quais registros satisfazem cada regra.
- Gerar um relatório explicativo para cada registro.

## Contexto

Você recebeu uma lista de usuários representados como dicionários:
~~~python
usuarios = [
    {"nome": "Ana", "idade": 25, "renda": 3500, "inadimplente": False},
    {"nome": "Bruno", "idade": 17, "renda": 1200, "inadimplente": True},
    {"nome": "Carla", "idade": 32, "renda": 8000, "inadimplente": False},
]
~~~
E uma lista de regras de aprovação de crédito:
~~~python
regras = [
    "idade >= 18",
    "renda >= 3000",
    "inadimplente == False"
]
~~~
# O que você deve implementar

Crie uma função:
~~~python
def avaliar_usuarios(usuarios, regras):
~~~
Ela deve:
Avaliar cada usuário contra todas as regras.
Retornar uma estrutura contendo:
- Se o usuário foi aprovado (todas as regras verdadeiras).
- Quais regras passaram.
- Quais regras falharam.
- Uma explicação textual.

# Resultado Esperado (Exemplo)

~~~python
Para Ana:

Usuária: Ana
Regra idade >= 18 → True
Regra renda >= 3000 → True
Regra inadimplente == False → True

Status: APROVADO

Para Bruno:

Usuário: Bruno
Regra idade >= 18 → False
Regra renda >= 3000 → False
Regra inadimplente == False → False

Status: REPROVADO
~~~

# Restrições

- Não usar eval
- Não usar bibliotecas externas
- Deve interpretar a regra como string
- Deve suportar operadores: >, <, >=, <=, ==, !=
- Deve gerar explicação textual coerente