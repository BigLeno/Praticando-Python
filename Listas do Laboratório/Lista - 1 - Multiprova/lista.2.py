n = int(input())
pizzas = []
for i in range(0,n):
    nome = input()
    preço = float(input())
    ingredientes = input().split()

    pedidos = {
        'nome': nome,
        'preco': preço,
        'ingredientes': ingredientes
    }
    pizzas.append(pedidos)

ing = input()
maior_preco = 0
mais_cara = " "
for pizza in pizzas:
    if pizza['preco'] > maior_preco:
        mais_cara = pizza['nome']
        maior_preco = pizza['preco']
if mais_cara == " ":
    print("Nenhuma pizza tem "+ing)
else:
    print(mais_cara)