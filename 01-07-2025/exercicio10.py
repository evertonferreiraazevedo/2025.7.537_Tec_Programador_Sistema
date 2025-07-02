base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 1
for i in range(expoente):
    resultado *= base 
    print(f"{base}^{i+1} = {resultado}")