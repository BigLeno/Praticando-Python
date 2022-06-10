glossary = {
    'print()':'Um exemplo de saída',
    'input()':'Um exemplo de entrada',
    '.items()':'acessa os chave-valor de um dicionário',
    '.keys()':'acessa as chaves de um dicionário',
    '.values()':'acessa os valores de um dicionário'
}

for qtd,tmp in glossary.items():
    print(f'A funcionalidade de "{qtd}" é: "{tmp}"')