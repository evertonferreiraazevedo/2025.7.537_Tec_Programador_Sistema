# def preencher_lista(tamanho):
#     lista = []
#     for i in range(tamanho):
#         lista.append(i)
#     return lista

# def dividir_lista(lista):
#     par = []
#     impar = []
#     for i in range(len(lista)):
#         if lista[i] % 2 == 0:
#             par.append(lista[i])
#         else:
#             impar.append(lista[i])
#     return par, impar


# def main():
#     tamanho = int(input("Digite o tamanho da lista: "))
#     lista = preencher_lista(tamanho)
#     par, impar = dividir_lista(lista)
#     print("Lista par: ", par)
#     print("Lista impar: ", impar)

# main()

# Recebe o tamanho da lista
tamanho = int(input("Digite o tamanho da lista: "))

# Preenche a lista com números de 0 até o tamanho-1
lista = []
for i in range(tamanho):
    lista.append(i)

# Separa os números pares e ímpares
par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

# Exibe as listas
print("Lista par:", par)
print("Lista ímpar:", impar)
