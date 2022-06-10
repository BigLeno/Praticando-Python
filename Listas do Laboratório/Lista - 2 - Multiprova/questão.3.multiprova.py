ingredients = [input(), input(), input(), input()]

ingredients_added = [input()]

for x in ingredients_added:
	if x not in ingredients:
		ingredients.append(x)
		print('Colocando ' + x + ' na pizza')
	elif x in ingredients:
		print('Pizza já tem ' + x)

