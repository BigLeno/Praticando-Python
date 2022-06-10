def descreve_cidade(cidade, país):
    """Descrevendo cidades"""
    print(f'{cidade} está localizada no(a) {país}')

descreve_cidade(input('Insira sua cidade: ').title(), input('Insira o país: ').title())
descreve_cidade('Reykjavik', 'Islândia')