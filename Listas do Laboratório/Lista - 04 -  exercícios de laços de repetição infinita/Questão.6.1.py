prompt = "Bem vindo ao GordoGalado's Cinema "
print(prompt)

idade = input("Qual a sua idade? ")

while idade != 'sair':
    
    idade = int(idade)
    if idade < 3:
        print("O ingresso é gratuito!")
    elif idade >= 3 and idade <= 12:
        print("O ingresso custa 10 reais")
    else:
        print("O ingresso custa 15 reais")
        
    idade = input("Qual a sua idade? (se desejar não continuar, digite 'sair') ")
       