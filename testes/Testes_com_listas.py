# primeiro quando referenciamos alguma variavel, associamos ele a um dado na memória, ou sej a
a = "abacate"
#nesse caso abacate esta na memória e nos referenciamos a esse dado através da variavael a
print(a)
#>>> abacate
# quando pedimos para printar o valor que sai será a referencia da memória que fizemos.
# A string, é um tipo de dado imutavel no python, logo não conseguimos variar sua estrutura. sendo assim quando associamos outra
#variavel a string, e modificamos essa variavel não podemos variair a estrtura da string, apenas a relação que a associação faz.
b = 'abacate'
b = 'abacate' + ',jaca'
print(b)
print(a)
#>> abacate,jaca
#>> abacate
#-----------------------------------------------------------------------------------------------------------------------------------
# o mesmo não pode ser dito para listas, elas são mutaveis, então modificações nelas são feitas na estrutura da memória, perdendo a referencia original.

c = ["a","b","c"]
d = c

print(c)
print(d)
#modificamos a lista d, temos 
d.append("d")

print(c)
print(d)

#logo mudanças na variavel em tipo de dados mutaveis são aplicadas na raiz da memória
#mas e quando criamos duas listas com os mesmos elementos, ela é salva também na mesma memória? Não, o computador salva em blocos de memória diferente.
e = ["a","b","c"]
f = ["a","b","c"]

e.append("d")

print(e)
print(f)