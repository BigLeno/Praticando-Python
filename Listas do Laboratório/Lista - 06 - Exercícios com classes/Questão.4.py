class Restaurante:
    """Uma classe que descreve um restaurante"""

    def __init__(self, nome_do_restaurante, tipo_de_cozinha):
        self.nome = nome_do_restaurante.title()
        self.cozinha = tipo_de_cozinha.title()
        self.numero_de_clientes = 0

    def descreve_restaurante(self):
        print(f"O restaurante {self.nome} possui o tipo de cozinha de {self.cozinha}")

    def abre_restaurante(self):
        print(f"O {self.nome} está aberto!")

    def set_numero_de_clientes(self, qtdclientes):
        self.numero_de_clientes = qtdclientes

    def incrementa_numero_de_clientes(self, incremento):
        self.numero_de_clientes += incremento

restaurante = Restaurante(input("Qual é o nome do restaurante? "), input("Qual é o tipo de cozinha dele? "))

print(f"A quantidade de clientes atendidos é: {restaurante.numero_de_clientes}")

restaurante.set_numero_de_clientes(int(input("Digite a nova quantidade de clientes: ")))

print(f"A quantidade de clientes atendidos é: {restaurante.numero_de_clientes}")

restaurante.incrementa_numero_de_clientes(int(input("Qual a quantidade de clientes que foram servidos? ")))

print(f"A quantidade de clientes atendidos no dia foi: {restaurante.numero_de_clientes}")



