respostas = []

print(" Aconteceu um crime e você precisa responder a essas 5 perguntas ")
print("Responda sim ou não")

respostas.append(input("Telefonou para a vítima? "))
respostas.append(input("Esteve no local do crime? "))
respostas.append(input("Mora perto da vítima? "))
respostas.append(input("Devia para a vítima? "))
respostas.append(input("Já trabalhou com a vítima? "))

classificacao = respostas.count("sim")

if classificacao == 2:
    print("Você é suspeito")
elif classificacao == 3 or classificacao == 4:
    print("Você é cúmplice")
elif classificacao == 5:
    print("Você é o assassino")
else:
    print("Você é inocente")


