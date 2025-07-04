numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
cont = 0

if numero1 < numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1 += 1
        cont +=1
    print(f"Existem {cont} números no intervalo informado.")

elif numero2 < numero1:
    while numero2 <= numero1:
        print(numero2)
        numero2 += 1
        cont +=1
    print(f"Existem {cont} números no intervalo informado.")
else:
    print("Os números são iguais.")





# for i in range (numero1, numero2):
#     print(i)

# # for i in range(numero2, numero1):
# #     print(i)
