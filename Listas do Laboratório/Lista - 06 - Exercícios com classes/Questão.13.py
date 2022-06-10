from statistics import linear_regression


class OrderedDict :
    """Iniciando uma nova forma de organizar o glossário"""
    def __init__(self, glossario):
        """Começando a contar..."""
        self.glossario = glossario

    def adiciona_item (self, nome, valor):
        """Adicionando itens no glossário"""
        print('adicionando novos itens...')
        self.glossario[nome] = valor

    def descreve_glossario (self):
        """Descrevendo o galado... """
        print("Mostrando seu glossário... ")
        for qtd,tmp in self.glossario.items():
            print(f'A funcionalidade de "{qtd}" é: "{tmp}"')

glossary = {
    'print()':'Um exemplo de saída',
    'input()':'Um exemplo de entrada',
    '.items()':'acessa os chave-valor de um dicionário',
    '.keys()':'acessa as chaves de um dicionário',
    '.values()':'acessa os valores de um dicionário'
}

glossary['dicionary[x] = y'] = 'adiciona um padrão valor-chave em um dicionário'
glossary['lists = [ ]'] = 'cria uma lista vazia'
glossary['dicionary = { }'] = 'cria um dicionário vazio'
glossary['lists.append(x)'] = 'adiciona um item no final de uma lista'
glossary['lists.pop( )'] = 'retira o último item de uma lista'


livro_dos_cornos = OrderedDict(glossary)

livro_dos_cornos.descreve_glossario()

livro_dos_cornos.adiciona_item("len()", "Diz o tamanho da variável passada")
livro_dos_cornos.adiciona_item("Classe", "Cria um novo tipo de variável")
livro_dos_cornos.adiciona_item("def __init__(self, ...): ", "Função construtora de classes")
livro_dos_cornos.adiciona_item(".strip() ", "Retira os espaços de uma string")
livro_dos_cornos.adiciona_item("del excluido[1]", "Deleta a posição passada daquela lista") 

livro_dos_cornos.descreve_glossario()



































for qtd,tmp in glossary.items():
    print(f'A funcionalidade de "{qtd}" é: "{tmp}"')
