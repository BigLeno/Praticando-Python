favorite_numbers = {
    'camillo':
    [ 12,
    13,
    17
    ],
    'rodrigo':
    [21,
    14,
    18,
    ],
    'rutileno':
    [13,
    3,
    2003,
    ]

   
}

for key, value in favorite_numbers.items():
    print(f'\t Imprimindo os dados de {key}...')
    for qtd in value:
        print(f'Os números favoritos de {key} são: {qtd}')
