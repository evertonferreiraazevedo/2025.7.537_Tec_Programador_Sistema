eleitores = int(input("Digite a quantidade de eleitores votantes: "))
cont = 0
votosA = 0
votosB = 0
votosNulo =0

while cont != eleitores:
    voto = input("Digite o seu voto (A, B ou N): ")
    if voto == "A" or voto == "B" or voto == "N":
        print("Voto registrado com sucesso!")
        cont += 1
        if voto == "A":
           votosA += 1
        elif voto == "B":
            votosB += 1
        else:
            votosNulo += 1
    else:
        print("Voto inválido. Por favor, tente novamente.")
   
print("Resultado final: ")
print(f"Candidato A: {votosA} votos")
print(f"Candidato B: {votosB} votos")
print(f"Votos Nulo: {votosNulo} votos")