important_rivers = {
    'nilo':'egito',
    'amazonas':'brasil',
    'são francisco':'brasil'
}

for qtd,tmp in important_rivers.items():
    print(f'O "{qtd.title()}" corre pelo "{tmp.title()}"')

for qtd in important_rivers.keys():
    print(qtd)

for tmp in important_rivers.values():
    print(tmp)