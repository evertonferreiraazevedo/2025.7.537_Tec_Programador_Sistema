# #1 questao
# pessoa = {"nome": "Everton", "idade": 30, "cidade natal": "Fortaleza", "profissão": "Professor"}


# #2 questao
# print("Nome:", pessoa["nome"])
# print("Idade:", pessoa["idade"])


# #3 questao
# pessoa["profissão"] = "Desenvolvedor"
# print(pessoa)

# #4 questao
# pessoa["email"] = "Everton@email.com"
# pessoa["telefone"] = "99999-9999"
# print(pessoa)


# #5 questao 
# del pessoa["telefone"]
# print(pessoa)

#6 questao
amigos = {
    "Mirela": 24,
    "Isaac": 29,
    "Elton": 39,
    "Matheus": 27
}

for nome, idade in amigos.items():
    print(f"{nome} tem {idade} anos.")


#7 questao

nome_busca = input("Digite o nome do amigo: ")

if nome_busca in amigos:
    print("Amigo encontrado.")
else:
    print("Amigo não encontrado.")


#8 questao
quantidade = len(amigos)
print(f"Total de amigos cadastrados: {quantidade}")
