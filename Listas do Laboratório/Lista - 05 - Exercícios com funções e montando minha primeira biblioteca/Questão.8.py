def faz_album(artista, album, qtd_faixas, faixas):
    """Fazendo um álbum"""
    albun = {
        'autor': artista,
        'album': album,
        'faixas': faixas
    }
    for chave, valor in albun.items():
        autor = albun['autor']
        nome_album = albun['album']
        faixas = albun['faixas']
    formatado = f'O autor de {nome_album} é {autor}, o álbum possui {qtd_faixas} faixas e elas são: {faixas}'
    return formatado

artist = ""
name = ""
faixas = []
qtd_faixas = ""

while True:
    if artist != "parar" or artist != "Parar":
        artist = input("Diga- me o o nome do artista (se quiser parar, digite 'parar'): ").title()
        if artist == "parar" or artist == "Parar":
            break
        name = input("Diga-me o nome do album: ")
        qtd_faixas = int(input('Quantas faixas esse album possui? '))

        for qtd in range(0, qtd_faixas):
            faixa = ""
            faixa = input("Diga-me uma: ").title()
            faixas.append(faixa)

        s = faz_album(artist , name, qtd_faixas, faixas)
        print(s)
    else:
        break

