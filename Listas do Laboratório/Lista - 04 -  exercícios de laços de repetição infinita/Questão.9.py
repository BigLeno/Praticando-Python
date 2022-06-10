pedidos_de_sanduiche = ['atum', 'pastrami', 'frango', 'carne', 'pastrami', 'vegano', 'pastrami']
sanduiches_prontos = []

print("A lanchonete está sem pastrami")

while 'pastrami' in pedidos_de_sanduiche:
    pedidos_de_sanduiche.remove('pastrami')



while pedidos_de_sanduiche:
    print(f"Pedidos de sanduiches: {pedidos_de_sanduiche}")
    print(f"Sanduiches prontos: {sanduiches_prontos}")

    print(f"Preparando seu sanduiche de {pedidos_de_sanduiche[0]}")

    sanduiches_prontos.append(pedidos_de_sanduiche[0])

    del pedidos_de_sanduiche[0]

print(f"Sanduiches prontos: {sanduiches_prontos}")


