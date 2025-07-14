# Uma UBS possui um estoque de vacinas com os seguintes lotes (quantidades): [120, 85, 100, 50, 95]. Crie um programa que remova o lote com menor quantidade e adicione um novo lote com 130 unidades. Mostre o estoque final.

estoque = [120, 85, 100, 50, 95]
print("Estoque inicial:", estoque)

temp = sorted(estoque)
estoque.remove(temp[0])
#estoque.remove(min(estoque))

estoque.append(130)
print("Estoque final:", estoque)
