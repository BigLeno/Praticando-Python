class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = {}
    
    def adiciona(self, nome):
        print(f'{nome} adicionado ao catálogo')
        self.catalogo[nome] = 'disponível'
    
    def emprestimo(self, nome):
        if nome in self.catalogo.keys():
            if self.catalogo[nome] == 'disponível':
                print(f'{nome} emprestado')
                self.catalogo[nome] = 'emprestado'
            else:
                print(f'{nome} já foi emprestado')
        else:
            print(f'{nome} não está no catálogo')
            
    def mostra_catalogo(self):
        print(self.nome)
        for tit, disp in self.catalogo.items():
            print(f'{tit} ({disp})')

nome = input()
biblioteca = Biblioteca(nome)
n = int(input())

for a in range(n):
    comando = input().split()
    if comando[0] == 'adicionar':
        biblioteca.adiciona(comando[1])
    elif comando[0] == 'emprestar':
        biblioteca.emprestimo(comando[1])
    elif comando[0] == 'imprimir':
        biblioteca.mostra_catalogo()
    else:
        print("Comando inválido")