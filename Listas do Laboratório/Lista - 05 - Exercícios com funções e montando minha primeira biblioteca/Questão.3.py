prompt1 = "Qual o tamanho de seua camiseta? "
prompt2 = "e qual o número dela? "

def faz_camiseta(tamanho, numero):
    """fazendo camisetas"""
    print(f'camisa {tamanho}, camisa {numero}')

faz_camiseta(input(prompt1), input(prompt2))