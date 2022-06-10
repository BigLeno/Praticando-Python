prompt = 'Bem vindo a pizzaria do Galado...'
prompt += '\nIniciando o seu pedido...'
print(prompt)

while True:
    ingrediente = input("Qual o ingrediente dessa vez? (para finalizar o laço, digite 'sair') ")
    if ingrediente != 'sair':
        print(f'Adicionando o {ingrediente} na sua pizza...')
    else:
        break



