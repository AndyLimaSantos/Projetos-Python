# Desafio Python — Simulador de Sistema de Cache (LRU)
## Objetivo

Implemente uma estrutura de dados que simule um cache com política LRU (Least Recently Used).

## Contexto

Um sistema precisa armazenar resultados de consultas para evitar recomputações caras.

O cache possui:
- Capacidade máxima fixa (ex: 3 itens)
- Operações:

        get(chave)
        put(chave, valor)

Quando o cache atingir a capacidade máxima:

O item menos recentemente utilizado deve ser removido.

## O que você deve implementar

Crie uma classe:

~~~python
class LRUCache:
    def __init__(self, capacity: int):
        pass
    
    def get(self, key: int) -> int:
        pass
    
    def put(self, key: int, value: int) -> None:
        pass
~~~
Regras:

1. get(key):

    - Retorna o valor se existir
    - Caso contrário, retorna -1
    - Marca o item como recentemente usado

2. put(key, value):

    - Se a chave já existir → atualiza valor e marca como recente
    - Se não existir:
    - Se houver espaço → adiciona

---
## Exemplo:
~~~python
cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
cache.get(1)      # retorna 10
cache.put(3, 30)  # remove chave 2
cache.get(2)      # retorna -1
cache.get(3)      # retorna 30
~~~

## Restrição Importante

Sua solução deve ter:

    - Complexidade O(1) para get
    - Complexidade O(1) para put

Ou seja:

- Não pode percorrer lista inteira
- Não pode ordenar a cada operação