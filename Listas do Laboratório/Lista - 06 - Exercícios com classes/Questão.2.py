class Restaurante:
    """Uma classe que descreve um restaurante"""

    def __init__(self, nome_do_restaurante, tipo_de_cozinha):
        self.nome = nome_do_restaurante.title()
        self.cozinha = tipo_de_cozinha.title()

    def descreve_restaurante(self):
        print(f"O restaurante {self.nome} possui o tipo de cozinha de {self.cozinha}")

    def abre_restaurante(self):
        print(f"O {self.nome} está aberto!")

restaurante1 = Restaurante(input("Qual é o nome do restaurante? "), input("Qual é o tipo de cozinha dele? "))
restaurante2 = Restaurante(input("Qual é o nome do restaurante? "), input("Qual é o tipo de cozinha dele? "))
restaurante3 = Restaurante(input("Qual é o nome do restaurante? "), input("Qual é o tipo de cozinha dele? "))

restaurante1.descreve_restaurante()
restaurante2.descreve_restaurante()
restaurante3.descreve_restaurante()