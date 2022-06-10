prompt = "Bem vindo ao GordoGalado's Cinema "
print(prompt)

while True:
    idade = input("Qual a sua idade? (se desejar sair, digite 'sair') ")
    if idade != 'sair':
        idade = int(idade)
        if idade < 3:
            print("O ingresso é gratuito!")
        elif idade >= 3 and idade <= 12:
            print("O ingresso custa 10 reais")
        else:
            print("O ingresso custa 15 reais")
    else:
        break