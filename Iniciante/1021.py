def Separa(valor):
    valor_int = int(valor)
    valor_centavos = valor*100 - valor_int*100 
    
    print(valor_int,valor_centavos)
    return [valor_int, valor_centavos]
    
def N_notas(valor, moedas):
    N_aparicoes = [0,0,0,0,0,0]
    notas_presentes = [100,50,20,10,5,2]
    for i in range(len(notas_presentes)):
        n_apari = valor//notas_presentes[i]
        valor = valor%notas_presentes[i]
        N_aparicoes[i] =int(N_aparicoes[i]+n_apari)

    moedas = moedas + (valor*100)
    N_aparicoes_moedas = [0,0,0,0,0,0]
    moedas_presentes = [100,50,25,10,5,1]
    for i in range(len(moedas_presentes)):
        n_apari_moedas = moedas//moedas_presentes[i]
        moedas = moedas%moedas_presentes[i]
        N_aparicoes_moedas[i] =int(N_aparicoes_moedas[i]+n_apari_moedas)

    return [N_aparicoes, N_aparicoes_moedas]



nota = Separa(float(input()))
valor_int, valor_centavos = N_notas(nota[0],nota[1])[0], N_notas(nota[0],nota[1])[1]

print(f'NOTAS:\n{valor_int[0]} nota(s) de R$ 100.00\n{valor_int[1]} nota(s) de R$ 50.00\n{valor_int[2]} nota(s) de R$ 20.00\n{valor_int[3]} nota(s) de R$ 10.00\n{valor_int[4]} nota(s) de R$ 5.00\n{valor_int[5]} nota(s) de R$ 2.00\nMOEDAS:\n{valor_centavos[0]} moeda(s) de R$ 1.00\n{valor_centavos[1]} moeda(s) de R$ 0.50\n{valor_centavos[2]} moeda(s) de R$ 0.25\n{valor_centavos[3]} moeda(s) de R$ 0.10\n{valor_centavos[4]} moeda(s) de R$ 0.05\n{valor_centavos[5]} moeda(s) de R$ 0.01')


