favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

lista_names = ['jen','sarah', 'edward', 'camillo', 'rutileno',  'phill']

for qtd in lista_names:
    if qtd in favorite_languages:
        print(f'tchau {qtd}, obrigado!')
    else:
        print(f'responda você também {qtd}!')
