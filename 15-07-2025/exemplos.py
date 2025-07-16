frutas = {"Manga": 10, "Abacate": 5, "Banana": 20, "Maca": 15}

# print(frutas["Banana"])
# print(frutas["Maca"])

# frutas["Melancia"] = 30
# print(frutas["Melancia"])

# print(frutas)
# if "Abacate" in frutas:
#     print("Tem Abacate")
# else:
#     print("Não tem Abacate")

# del frutas["Abacate"]

# if "Abacate" in frutas:
#     print("Tem Abacate")
# else:
#     print("Não tem Abacate")

# chaves = frutas.keys()
# valores = frutas.values()
# itens = frutas.items()

# print(chaves)   # Saída: 
# print(valores)  # Saída: 
# print(itens)    # Saída: 

# Iterando sobre as chaves
# for chave in frutas:
#     print(chave, frutas[chave])

# Iterando sobre os itens (chave, valor)
for chave, valor in frutas.items():
    print(chave, valor)

