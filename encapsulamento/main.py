class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self,):
       return self.ataque * 1


class Guerreiro(Personagem):
    def atacar(self):
        dano = self.ataque * 2
        print(f"O Nairon atacou Beatriz {dano}")

class Mago(Personagem):
    def atacar(self):
       dano = self.ataque * 3 

class Arqueiro:
    def atacar(self):
        dano = self.ataque * 1.5

guerreiro = Guerreiro("Thor", 100, 20)
mago = Mago("Merlin", 80, 20)
arqueiro = Arqueiro("Robin", 90, 20)  


personagens = [guerreiro, mago, arqueiro]

for personagem in personagens:
    personagem.atacar()