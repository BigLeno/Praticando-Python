pessoa1 = {
    'nome':'Rutileno',
    'sobrenome':'Gabriel',
    'cidade':'Natal',
    'idade':19,
}

pessoa2 = {
    'nome':'Rutileno',
    'sobrenome':'Gabriel',
    'cidade':'Natal',
    'idade':19,
}

pessoa3 = {
    'nome':'Rutileno',
    'sobrenome':'Gabriel',
    'cidade':'Natal',
    'idade':19,
}

listsofnames = []

listsofnames.append(pessoa1)
listsofnames.append(pessoa2)
listsofnames.append(pessoa3)

for qtd in listsofnames:
    for key, value in pessoa1.items():
        print(key, value)
    for key, value in pessoa2.items():
        print(key, value)
    for key, value in pessoa3.items():
        print(key, value)