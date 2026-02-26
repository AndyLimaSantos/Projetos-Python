Notas = input().split()
Media_principal = (float(Notas[0])*2 + float(Notas[1])*3 + float(Notas[2])*4 + float(Notas[3]))/10

if Media_principal >= 7:
    '''print do aluno aprovado'''
    print(f'Media: {Media_principal:.1f}\nAluno aprovado.')
elif Media_principal < 5:
    print(f'Media: {Media_principal:.1f}\nAluno reprovado.')
elif Media_principal >= 5 and Media_principal <= 6.9:
    '''print do aluno estar em exame'''
    Nota_exame = float(input())
    nova_media = (Media_principal+Nota_exame)/2
    if Media_principal >= 5:
        texto = 'Aluno aprovado.'
    else:
        texto = 'Aluno reprovado.'
    print(f'Media: {Media_principal:.1f}\nAluno em exame.\nNota do exame: {Nota_exame:.1f}\n{texto}\nMedia final: {nova_media:.1f}')
