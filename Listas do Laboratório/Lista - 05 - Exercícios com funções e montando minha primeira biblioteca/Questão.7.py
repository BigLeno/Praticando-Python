def faz_album(artista, album, qtd_faixas):
    """Fazendo um álbum"""
    faixas = []
    for qtd in range(0, qtd_faixas):
        faixa = input("Diga-me uma: ").title()
        faixas.append(faixa)
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

s = faz_album(input("Qual o nome do artista? ").title(), input("Qual o nome do album? ").title(), int(input('Quantas faixas esse album possui? ')))
print(s)