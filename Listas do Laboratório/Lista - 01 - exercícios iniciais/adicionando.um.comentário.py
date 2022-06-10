
#Este programa é responsável por exibir a mensagem de uma pessoa famosa...
#porém transformando toda a frase em uma só variável, para facilitar o print()...
#somente fazendo o que a questão pede, com as minhas maneiras de aplicar..
#a linguagem Python para a resolução da mesma!

#adicionando a pessoa famosa a uma variável de mesmo nome...
pessoa_famosa = 'Vinicius de Moraes'

#criando as varáveis para facilitar o uso do .format()...
frase1 = 'A vida é a arte do encontro, embora haja tanto desencontro pela vida.'

frase2 = ' certa vez disse: '

#dando significado a 'mensagem', da maneira que a questão pede...
mensagem = '{} {} "{}"'.format(pessoa_famosa, frase2, frase1)

#finalmente, exibindo a mensagem que a questão pede...
print(str(mensagem))

#fim!

