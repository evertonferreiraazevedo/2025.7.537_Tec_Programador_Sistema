#numero primo
numero = int(input("Digite um numero: "))

cont = 0
controle = 1

while controle <= numero:
    if numero % controle == 0:
        cont += 1
        controle += 1
    else:
        controle += 1

if cont == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")

# for i in range(1, numero+1):
#     if numero % i == 0:
#         cont +=1
#     else:
#         cont+1
# if cont == 2:
#     print(f"O número {numero} é primo.")
# else:
#     print(f"O número {numero} não é primo.")