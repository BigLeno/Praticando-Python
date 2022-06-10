import random

n = int(input('Entre com a quantidade de metas diárias: '))

daily_goal = []

dedicated_time = ['10min', '15min', '20min', '25min', '30min']
dedicated_hours = ['1hr', '2hr']
break_time = [*dedicated_time]

for qtd in range(0, n):
	question1 = input('Entre com a meta diária: ')
	daily_goal.append(question1)

tmp1 = random.choice(daily_goal)
tmp2 = random.choice(dedicated_time)
tmp3 = random.choice(dedicated_hours)
tmp4 = random.choice(break_time)

tpc1 = tmp3 + ' ' + tmp2 + ' ' + tmp1
tpc2 = tmp4 + ' ' + 'de descanso!'

print(tpc1)
print(tpc2)


	
