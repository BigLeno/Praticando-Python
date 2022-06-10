class Usuario:
    """Monta um usuário"""

    def __init__(self, primeiro_nome, ultimo_nome):
        """Inicializando os dados de uma pessoa"""
        self.primeiro_nome = primeiro_nome.title()
        self.ultimo_nome = ultimo_nome.title()
        self.idade = 19
        self.sexo = 'M'

    def descreve_usuario(self):
        print(f"O {self.primeiro_nome} {self.ultimo_nome}, possui {self.idade} anos de idade e é do sexo {self.sexo}")

    def cumprimenta_usuario(self):
        print(f"Seja bem-vindo {self.primeiro_nome} {self.ultimo_nome} ao nosso sistema!")

rogerin = Usuario(input("Digite seu primeiro nome: "), input("Digite seu último nome: "))

rogerin.cumprimenta_usuario()
rogerin.descreve_usuario()


