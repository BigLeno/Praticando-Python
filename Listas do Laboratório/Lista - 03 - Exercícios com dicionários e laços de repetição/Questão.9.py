lugares_favoritos = {
    'camillo':
    [ 'orlando',
    'redinha',
    'camurupim'
    ],
    'rodrigo':
    ['golandim',
    'bairro nordeste',
    'quintas',
    ],
    'rutileno':
    ['maiame',
    'dos artistas',
    'do forte',
    ]

   
}

for key, value in lugares_favoritos.items():
    print(f'Imprimindo os dados de {key}...')
    for qtd in value:
        print(f'{key} frequenta {qtd}')
