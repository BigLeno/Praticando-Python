def mostra_magicos(magicos):
    for magico in magicos:
        s = f"Aqui está o seu mágico: {magico.title()}"
        print(s)

def torna_grandioso(magicos):
    for indice in range(len(magicos)):
        magicos[indice] = f"O Grande {magicos[indice].title()}"
    

magicos = [input("Diga o nome de um mágico: "), input("Diga o nome de um mágico: "), input("Diga o nome de um mágico: ")]
mostra_magicos(magicos)
torna_grandioso(magicos)
mostra_magicos(magicos)
