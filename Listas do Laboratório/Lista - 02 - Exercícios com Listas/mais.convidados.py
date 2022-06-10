name = ['Érika', 'Cláudia', 'renatinha']

name.insert(0, 'flavinha')
name.insert(2, 'robertinha')
name.append('fernandinha')
print(name)
nome1 = name[0].title()
nome2 = name[1].title()
nome3 = name[2].title()
nome4 = name[3].title()
nome5 = name[4].title()
nome6 = name[5].title()

msg1 = 'Olá '
msg2 = ', você aceita ir jantar comigo?'
msg3 = 'diz: "é claro que posso!"'

print('{} {}{}'.format(msg1, nome1, msg2))
print('{} {}'.format(nome1,msg3))

print('{} {}{}'.format(msg1, nome2, msg2))
print('{} {}'.format(nome2,msg3))

print('{} {}{}'.format(msg1, nome3, msg2))
print('{} {}'.format(nome3,msg3))

print('{} {}{}'.format(msg1, nome4, msg2))
print('{} {}'.format(nome4,msg3))

print('{} {}{}'.format(msg1, nome5, msg2))
print('{} {}'.format(nome5,msg3))

print('{} {}{}'.format(msg1, nome6, msg2))
print('{} {}'.format(nome6,msg3))
