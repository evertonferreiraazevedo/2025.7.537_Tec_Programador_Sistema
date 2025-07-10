def substituir_numero(lista):
    for i in lista:
        if lista [i] % 2 == 0:
            lista[i] = 0
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(substituir_numero(lista))