#primeiro a gente faz uma biblioteca com todos os itens referenciados, o bom da biblioteca é a falta de necessidade de ordem
produtos = {1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
compras = input().split()
codigo, unidades = int(compras[0]), int(compras[1])
Total = unidades*produtos[codigo]
print(f'Total: R$ {Total:.2f}')