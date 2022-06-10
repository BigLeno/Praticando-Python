from tkinter import W


qtd_pessoas = int(input("Quantas pessoas estão participando da enquete? "))

prompt = "Se pudesse visitar um lugar no mundo, para onde você iria? "

lugares = []

while qtd_pessoas != 0:
    qtd_pessoas -= 1

    lugares.append(input(prompt).title())

print(lugares)

