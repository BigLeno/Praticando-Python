def olx_anuncio(marca, modelo, ano, cambio, **propriedades):
    """Fazendo anuncios de carros usados"""
    propriedades['marca'] = marca.upper()
    propriedades['modelo'] = modelo.title()
    propriedades['ano'] = ano
    propriedades['câmbio'] = cambio.title()

    return propriedades
    