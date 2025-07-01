base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 0
for i in range(1, expoente + 1):
    resultado += base

print(f"{base}^{expoente} = {resultado}")
