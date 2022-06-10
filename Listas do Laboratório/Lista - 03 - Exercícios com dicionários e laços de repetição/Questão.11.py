cities = {
    'Natal': {
        'população': '890.480',
        'país': 'Brasil',
        'curiosidade':'"galado"'
    },
    'Tokyo':{
        'população':'37.000.000',
        'país':'Japão',
        'curiosidade':'considerada a cidade mais habitável do mundo'
    },
    'Porto': {
        'população':'214.349',
        'país':'Portugal',
        'curiosidade':'segunda maior cidade'
    }
}

for city, data in cities.items():
    population = data['população']
    country = data['país']
    curiosity = data['curiosidade']
    print(f'Dados sobre a população de {city}, que é: {population}')
    print(f'Este é o país de {city}, que é: {country}')
    print(f'Esta é uma curiosidade de {curiosity}, que é: "{curiosity}"')
   

