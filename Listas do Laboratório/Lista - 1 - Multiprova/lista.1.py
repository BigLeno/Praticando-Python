pizzas = []
while True:
    nome = input("Qual o sabor desejado: ")
    if nome != 'sair':
        pedido = {
            'nome': nome,
            'preco':int(input("Qual o valor da pizza? ")),
            'ingredientes':input("Quais ingredientes desejados ").split(',')
        }
        pizzas.append(pedido.copy())
    else:
        break

for p in pizzas:
    print('Pizzas pedidas:')
    print(f"{p['nome']} (R$ {p['preco']}): {p['ingredientes']}")