N = int(input("Digite um número N: "))
soma = 0
for contador in range(1, N+1):
    soma = soma + contador
print(f"A soma dos números de 1 a {N} é: {soma}")