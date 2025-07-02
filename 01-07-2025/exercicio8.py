frase = input("Digite uma frase: ")
contador = 0
for letra in frase:
    if letra != " ":
        contador += 1

print(f'O número de caracteres (excluindo espaços) é: {contador}')
