valores_original=input().split()
lista_numerica = []
for i in range(len(valores_original)):
    lista_numerica.append(int(valores_original[i]))
lista_crescente = sorted(lista_numerica)
impressao = ''
for i in range(len(lista_crescente)):
    impressao += f'{lista_crescente[i]}\n'
impressao += '\n'
for i in range(len(lista_crescente)):
    impressao += f'{lista_numerica[i]}\n'

print(impressao[:-1])

