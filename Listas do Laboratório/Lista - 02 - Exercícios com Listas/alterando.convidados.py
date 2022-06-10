name = ['regina', 'Érika', 'Cláudia']

name2 = [*name, 'renatinha']

nome1 = name[0].title()
nome2 = name[1].title()
nome3 = name[2].title()

msg1 = 'Olá '
msg2 = ', você aceita ir jantar comigo?'
msg3 = 'Infelizmente '
msg4 = ' não poderá comparecer.'
msg5 = 'diz: "é claro que posso!"'

print('{} {}{}'.format(msg1, nome1, msg2))
print('{} {}{}'.format(msg3, nome1, msg4))

print('{} {}{}'.format(msg1, nome2, msg2))
print('{} {}'.format(nome2,msg5))

print('{} {}{}'.format(msg1, nome3, msg2))
print('{} {}'.format(nome3,msg5))



ausente = name2.remove('regina')
nome4 = name2[2].title()

print('{} {}{}'.format(msg1, nome4, msg2))
print('{} {}'.format(nome4,msg5))

lista_novos_convidados = name2

#lista de convidados anterior
print(name)

#lista de convidados atualizada
print(lista_novos_convidados)






