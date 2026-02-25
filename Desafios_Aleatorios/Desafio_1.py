'''
Inicialmente teremos que fazer sem utilizar bibiotecas externas, no entanto
sabemos que podemos colocar uma leitura de uma arquivo externo ou um banco 
de dados onine 
'''
#-------------------------tratamento dos dados para o problema------------------
'''
bancoDados = [
    {"nome": "Ana", "idade": 25, "renda": 3500, "inadimplente": False},
    {"nome": "Bruno", "idade": 17, "renda": 1200, "inadimplente": True},
    {"nome": "Carla", "idade": 32, "renda": 8000, "inadimplente": False},
]
'''
# Cada item da lista é uma biblioteca no entanto só possuimos 3 chaves
# nome, idade, renda
# possuimos apenas um problema em uma lista como saber qual a posição do usuário que procuramos
# Um caminho lógico é escrevendo um novo banco de dados com as informações escritas de maneira correta
# Outro caminho é escrevendo uma planilha ou um array, mas isso não bate com a restrição
# Outro caminho é fazer um verificador que vai percorrer todos os elementos da lista esse é o pior jeito 
# pois dependendo do tamano da lista o programa demorar alguns segundos
# Uma possibilidade bem confusa e criar uma key pelo nome e inserir as bibliotecas de cada um desses elemento dentro dessa key
# confuso mas aplicavel para listas extensas

# 1° Utilizando a transformação da lista em um dict
'''
bancoDados_dict = {}
for i in range(len(bancoDados)):
    bancoDados_dict[bancoDados[i]["nome"]] = bancoDados[i]
'''
#-------------------------tratamento das regras passadas-------------------
'''
regras = [
    "idade >= 18",
    "renda >= 3000",
    "inadimplente == False"
]
'''
#recebemos 3 regras, cada regra tem operadores lógicos, no entanto elas são separadas em espaços o que é bom
#As duas primeiras regras são núméricas e a última é um booleano
def separa_regras(regras):
    regras_dict ={}
    for i in range(len(regras)):
        analise = regras[i].split()
        if analise[0] == 'idade': #Analisa qual regra é
            cond_idade = condicional(analise[1])
            regras_dict['idade'] = [int(analise[2]), cond_idade]

        elif analise[0] == 'renda': #Analisa qual regra é
            cond_renda = condicional(analise[1])
            regras_dict['renda'] = [int(analise[2]), cond_renda]

        elif analise[0] == 'inadimplente': #Analisa qual regra é
            cond_inad = condicional(analise[1])
            if analise[2] == "False":
                regras_dict['inadimplente'] = [False, cond_inad]
            elif analise[2] == "True":
                regras_dict['inadimplente'] = [True, cond_inad]
    return regras_dict #{idade:[N°, cond_idade], renda:[N°, cond_renda], inadimplente:[boll, cond_inad] }

def condicional(operador): #verifica o operador existente em cada uma das regras
    condicionais = [">","<",">=","<=","==","!="]
    for i in range(len(condicionais)):
        if operador == condicionais[i]:
            return i
    return None

def condiciona_execute(n_cond, valor, valor_esperado):
    if n_cond == 0:
        return valor > valor_esperado
    elif n_cond == 1:
        return valor < valor_esperado
    elif n_cond == 2:
        return valor >= valor_esperado
    elif n_cond == 3:
        return valor <= valor_esperado
    elif n_cond == 4:
        return valor == valor_esperado
    elif n_cond == 5:
        return valor != valor_esperado

#------------------------ inicio do código --------------------------------
def avaliar_usuarios(usuarios, regras):
    #verificamos a idade
    regras_formatadas = separa_regras(regras)
    for i in range(len(usuarios)):
        #verificando a idade
        condiciona_idade = condiciona_execute(n_cond=regras_formatadas["idade"][1] , valor=usuarios[i]["idade"], valor_esperado=regras_formatadas["idade"][0])
        #verificando a renda
        condiciona_renda = condiciona_execute(n_cond=regras_formatadas["renda"][1] , valor=usuarios[i]["renda"], valor_esperado=regras_formatadas["renda"][0])
        #verificando a inadimplente
        condiciona_inadimplencia = condiciona_execute(n_cond=regras_formatadas["inadimplente"][1] , valor=usuarios[i]["inadimplente"], valor_esperado=regras_formatadas["inadimplente"][0])
        #Status
        if condiciona_idade == True and condiciona_renda == True and condiciona_inadimplencia == True:
            status = "APROVADO"
        else:
            status = "REPROVADO"        
        print(f"Usuario: {usuarios[i]["nome"]}\nRegra de {regras[0]} -> {condiciona_idade}\nRegra de {regras[1]} -> {condiciona_renda}\nRegra de {regras[2]} -> {condiciona_inadimplencia}\n\nStatus: {status}\n")
    return None

def main():
    bancoDados = [
    {"nome": "Ana", "idade": 25, "renda": 3500, "inadimplente": False},
    {"nome": "Bruno", "idade": 17, "renda": 1200, "inadimplente": True},
    {"nome": "Carla", "idade": 32, "renda": 8000, "inadimplente": False},
    ]
    regras = [
    "idade >= 18",
    "renda >= 3000",
    "inadimplente == False"
    ]
    avaliar_usuarios(bancoDados, regras)


if __name__ == "__main__":
    main()