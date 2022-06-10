robertinho = {
    'nome':'robertinho',
    'tipo':'cão',
    'dono':'cleiton'
}
claudinho = {
    'nome':'claudinho',
    'tipo':'pássaro',
    'dono':'roberval'
}
matheus = {
    'nome':'matheus',
    'tipo':'burro',
    'dono':'camillo'
}

pets = []

pets.append(robertinho)
pets.append(claudinho)
pets.append(matheus)

for qtd in pets:
    for key, value in robertinho.items():
        print(f'O {key} = {value}')
    