def cidade_pais(cidade, país):
    """Conjunto de cidades_país"""
    cidade_país = f'{cidade}, {país}'
    return cidade_país
   
s = cidade_pais(input('Insira a cidade: ').title(), input('Insira o país: ').title())
print(s)