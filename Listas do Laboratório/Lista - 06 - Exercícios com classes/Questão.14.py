from random import randint

x = randint (1, 6)

class Dado:
    """Criando dados"""
    def __init__(self, lados = 6):
        """Você tem dado em casa? """
        self.lados = lados
        print(f"O seu dado tem {self.lados} lados... ")

    def joga_dado(self, qtd =1 ):
        """Joga demais, ô fi de rapariga pra jogar """
        print("Jogando o seu dado...")
        for a in range(qtd):
            print(f"O valor foi {randint(1, self.lados)}")

dado = Dado()
dado.joga_dado(10)

dado20 = Dado(20)
dado20.joga_dado(10)

