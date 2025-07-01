# inicio = int(input("Digita ai o inicio: "))
# fim = int(input("Digita ai o fim: "))

# for i in range(inicio, fim, 2):
#     print(i)

# for i in range(fim):
#     if i % 2 == 1:
#         print(i)

# Receba 5 números e determine o maior
for i in range(5):
    num = int(input("Digite um número: "))
    if i == 0:
        maior = num
    else:
        if num > maior:
            maior = num
print("O maior número é:", maior)

# Receba 5 números e determine o menor
for i in range(5):
    num = int(input("Digite um número: "))
    if i == 0:
        menor = num
    else:
        if num < menor:
            menor = num
print("O Menor número é:", menor)




