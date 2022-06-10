def faz_hamburguer(*ingredientes):
    """Fazendo Hambúrguer"""
    print("Iniciando o pedido... ")
    print("O seu pedido terá: ")
    for ingrediente in ingredientes:
        print(ingrediente)

qtd_ingredientes = int(input("Quantos ingredientes você deseja: "))

ingredientes = []

for tmp in range(qtd_ingredientes):
    ingredientes.append(input("Qual o ingrediente que você deseja? ").title())

faz_hamburguer(ingredientes)
