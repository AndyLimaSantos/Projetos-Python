from classe_personagem import Personagem

personagem_1 = Personagem("Luis", 100, 10, 30)
personagem_2 = Personagem("Larissa", 100, 50, 50)

personagem_1.dano(personagem_2.ataque)

personagem_1.print()
personagem_2.print()

personagem_1.dano(personagem_2.ataque)