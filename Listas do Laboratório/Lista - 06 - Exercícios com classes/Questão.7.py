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

class Admin(Usuario):
    """O administrador está online"""

    def __init__(self, primeiro_nome, ultimo_nome, privilegios):
        super().__init__(primeiro_nome, ultimo_nome)
        self.privilegios = privilegios

    def mostra_privilegios(self):
        print(f"Os privilegios do administrador são: {self.privilegios}")

    def descreve_usuario(self, cargo):
        self.cargo = cargo
        print(f"O {self.primeiro_nome} {self.ultimo_nome}, possui {self.idade} anos de idade e é do sexo {self.sexo} e tem o cargo de {self.cargo}")
        

rogerin = Admin(input("Digite seu primeiro nome: "), input("Digite seu último nome: "), ['pode adicionar postagem', 'pode apagar postagem', 'pode banir usuario', 'pode liberar a baderna'])

rogerin.cumprimenta_usuario()
rogerin.descreve_usuario("Administrador do Grupo")
rogerin.mostra_privilegios()
rogerin.mostra_privilegios()



