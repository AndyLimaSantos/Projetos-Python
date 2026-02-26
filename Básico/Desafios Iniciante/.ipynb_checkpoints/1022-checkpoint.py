'''
A tarefa aqui neste problema é ler uma expressão matemática na forma
 de dois números Racionais (numerador / denominador) e apresentar o
 resultado da operação. Cada operando ou operador é separado por um
 espaço em branco. A sequência de cada linha que contém a expressão
a ser lida é: número, caractere, número, caractere, número, caractere,
número. A resposta deverá ser apresentada e posteriormente simplificada.
Deverá então ser apresentado o sinal de igualdade e em seguida a resposta
simplificada. No caso de não ser possível uma simplificação, deve ser apresentada
a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação
de como deverá ser realizada cada uma das operações:

Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
'''
valor = input().split()

print(valor)