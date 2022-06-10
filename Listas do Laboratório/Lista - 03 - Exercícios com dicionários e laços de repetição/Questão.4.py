glossary = {
    'print()':'Um exemplo de saída',
    'input()':'Um exemplo de entrada',
    '.items()':'acessa os chave-valor de um dicionário',
    '.keys()':'acessa as chaves de um dicionário',
    '.values()':'acessa os valores de um dicionário'
}

for qtd,tmp in glossary.items():
    print(f'A funcionalidade de "{qtd}" é: "{tmp}"')

print('adicionando novos itens...' + '\n' + 'exibindo o novo glossário...')

glossary['dicionary[x] = y'] = 'adiciona um padrão valor-chave em um dicionário'
glossary['lists = [ ]'] = 'cria uma lista vazia'
glossary['dicionary = { }'] = 'cria um dicionário vazio'
glossary['lists.append(x)'] = 'adiciona um item no final de uma lista'
glossary['lists.pop( )'] = 'retira o último item de uma lista'

for qtd,tmp in glossary.items():
    print(f'A funcionalidade de "{qtd}" é: "{tmp}"')
