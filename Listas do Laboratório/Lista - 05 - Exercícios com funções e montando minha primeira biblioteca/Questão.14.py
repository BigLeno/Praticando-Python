def olx_anuncio(marca, modelo, ano, cambio, **propriedades):
    """Fazendo anuncios de carros usados"""
    propriedades['marca'] = marca.upper()
    propriedades['modelo'] = modelo.title()
    propriedades['ano'] = ano
    propriedades['câmbio'] = cambio.title()

    return propriedades

carro = olx_anuncio(input('Qual o marca do seu carro: '), input('Qual o modelo do seu carro: '), int(input('Qual o ano do seu carro: ')), input('Qual o câmbio do seu carro (Aut/Mt): '), estado = 'usado')
print(carro)