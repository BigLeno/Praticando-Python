def mostra_magicos(magicos):
    for magico in magicos:
        s = f"Aqui está o seu mágico: {magico.title()}"
        print(s)


magicos = [input("Diga o nome de um mágico: "), input("Diga o nome de um mágico: "), input("Diga o nome de um mágico: ")]
mostra_magicos(magicos)
