#Primeiro vamos criar uma classe, que corresponde a um personagem
#Para isso precisamos saber quais atributos tem um personagem, de maneira simples temos
#Personagem -> Vida, Ataque, Defesa e Bolsa <- esse é o simple sé o que faremso
class Personagem: #declaração da classe
    #declaração dos atributos
    def __init__(self, nome = "Romero Brito", vida = 100, ataque = 50, defesa = 50): #Método construtor
        #atributos da classe
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.bolsa = [] #Objetos na bolsa do personagem
        pass
    #declaração de métodos instanciaveis
    def dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} morreu")
        pass
    def cura(self, cura):
        self.vida += cura
        pass
    def print(self):
        print(f"Seus atributos são\nVida = {self.vida};\nAtaque = {self.ataque};\nDefesa = {self.defesa}.")
    
#Com isso criamos uma pequena classe para personagens.