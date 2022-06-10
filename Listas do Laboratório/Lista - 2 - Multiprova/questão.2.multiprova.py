n = int(input())

alunos_todos = []

for qtd in range(0, n):
	alunos_nomes = input()
	alunos_todos.append(alunos_nomes)

nomes_unicos = []

for x in alunos_todos:
	if x not in nomes_unicos:
		nomes_unicos.append(x)
		
print(alunos_todos)
print(nomes_unicos)
