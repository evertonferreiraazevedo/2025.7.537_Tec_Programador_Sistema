numero = 0
soma = 0
while numero >= 0:
    numero = int(input("Digite um número: "))
    if numero >= 0:
        soma += numero
    else:
        print("Número inválido")
        
print("Soma dos números positivos: ", soma)