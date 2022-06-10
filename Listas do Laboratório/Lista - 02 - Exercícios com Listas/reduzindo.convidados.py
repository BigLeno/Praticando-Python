name = ['flavinha', 'Érika', 'robertinha', 'Cláudia', 'renatinha', 'fernandinha']

msg1 = '"Infelizmente as reservas se esgotaram, agora só posso levar duas pessoas"'

print(msg1)

banido1 = name.pop(5)
banido2 = name.pop(4)
banido3 = name.pop(3)
banido4 = name.pop(2)

msg2 = 'Olá '
msg3 = ', sinto muito por não poder mais te levar!'

print('{} {}{}'.format(msg2, banido1, msg3))
print('{} {}{}'.format(msg2, banido2, msg3))
print('{} {}{}'.format(msg2, banido3, msg3))
print('{} {}{}'.format(msg2, banido4, msg3))

nome1 = name[0].title()
nome2 = name[1].title()

msg4 = ', você continua na lista!'

print('{} {}{}'.format(msg2, nome1, msg4))
print('{} {}{}'.format(msg2, nome2, msg4))

del name[1]
del name[0]

print(name)










