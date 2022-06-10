n = int(input())

starter_ingredients = []

for qtd in range(0, n):
	ingredients_added = [input(), input(), input()]
	starter_ingredients.append(ingredients_added[0])
	starter_ingredients.append(ingredients_added[1])
	starter_ingredients.append(ingredients_added[2])

additional_ingredient = [input()]
repeat_list = [] 
not_repeat_list = []
for tmp in starter_ingredients:
	if tmp not in additional_ingredient:
		not_repeat_list.append(tmp)
	else:
		repeat_list.append(tmp)

print(len(repeat_list))




