import olx_anunciar as olx

carro = olx.olx_anuncio(input('Qual o marca do seu carro: '), input('Qual o modelo do seu carro: '), int(input('Qual o ano do seu carro: ')), input('Qual o câmbio do seu carro (Aut/Mt): '), estado = 'usado')
print(carro)


