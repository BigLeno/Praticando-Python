def cria_dic(nome, valor):
    dic = {'nome':nome, 'valor':valor}
    return dic

def cabe_no_orcamento (pratos, orcamento):
    idx = []
    for a in range(len(pratos)):
        if pratos[a]['valor'] <= orcamento:
            idx.append(a)
            
    return idx

n = int(input())
pratos = []

for i in range(n):
    nome = input()
    valor = int(input())
    pratos.append(cria_dic(nome, valor))

orcamento = int(input())

resultado = cabe_no_orcamento(pratos, orcamento)

print("Pratos dentro do orçamento")

for a in resultado:
    print(f"{pratos[a]['nome']} {pratos[a]['valor']}")